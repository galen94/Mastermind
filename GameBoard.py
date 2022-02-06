'''
Galen Otten
CS 5001, Spring 2021
Final Project: MasterMind
This GameBoard Class creates
a gameboard that can display
the current game progress.
'''

import turtle
from Point import Point
from Gif import Gif
from Box import Box
from Marble import Marble
from LeaderBoard import LeaderBoard

BEGIN_MARBLE_ROW_X = -350
BEGIN_MARBLE_ROW_Y = 300
MARBLE_ROW_DISTANCE_X = 50
MARBLE_ROW_DISTANCE_Y = 45
MINI_MARBLE_SIZE = 5
BEGIN_MINI_MARBLE_ROW_X = -25
BEGIN_MINI_MARBLE_ROW_Y = 305
MINI_MARBLE_DISTANCE_X = 15
MINI_MARBLE_DISTANCE_Y = 15
MINI_MARBLE_GROUP_DISTANCE_Y = 15
COLOR_MARBLES_BEGIN_X = -380
COLOR_MARBLES_BEGIN_Y = -262
COLOR_MARBLES_DISTANCE_X = 50
CHECK_BUTTON_SIZE = 18
CHECK_BUTTON_POSITION_X = 25
CHECK_BUTTON_POSITION_Y = -250
X_BUTTON_SIZE = 18
X_BUTTON_POSITION_X = 100
X_BUTTON_POSITION_Y = -250
MARBLEBOARD_HEIGHT = 485
MARBLEBOARD_LENGTH = 450
MARBLEBOARD_WALL_WIDTH = 4
MARBLEBOARD_BEGIN_X = -375
MARBLEBOARD_BEGIN_Y = 300
CLICKBOARD_HEIGHT = 100
CLICKBOARD_LENGTH = 725
CLICKBOARD_WALL_WIDTH = 4
CLICKBOARD_BEGIN_X = -375
CLICKBOARD_BEGIN_Y = -200
QUIT_GIF_X = 275
QUIT_GIF_Y = -250
X_BUTTON_GIF_X = 100
X_BUTTON_GIF_Y = -250
CHECK_GIF_X = 25
CHECK_GIF_Y = -250
EMPTY_MARBLE_COLOR = "black"
NORMAL_BOX_COLOR = "black"
NUMBER_MINI_MARLBE_GROUPS = 10
NUMBER_IN_MINI_GROUP_TOP_ROW = 2
NUMBER_IN_MINI_GROUP_BOTTOM_ROW = 2
NUMBER_MARBLE_ROWS = 10
NUMBER_MARBLES_EACH_ROW = 4
QUITGIF_FILENAME = "smallerquit.gif"
X_BUTTON_FILENAME = "xbutton.gif"
CHECK_BUTTON_FILENAME = "checkbutton.gif"
COLORS = ["red", "blue", "green", "yellow", "purple", "black"]


    
class GameBoard:
    '''
    This GameBoard Class creates a gameboard
    that has a marbleboard, leaderboard, and
    clickboard. It includes methods to draw the
    guess marbles and mini peg marbles in the
    marbleboard, and colored marbles in the clickboard. 
    '''
    def __init__(self):
        '''
        This method creates an instance
        of a gameboard which has a marbleboard,
        leaderboard, clickboard, quit gif, x button gif,
        click button gif, the position of the x and check
        button gifs, game colors, and lists of all of
        the marble instances drawn over the gameboard. 
        Parameters: None
        Return: None, A gameboard instance
        '''
        self.marbleboard = Box(MARBLEBOARD_HEIGHT, MARBLEBOARD_LENGTH,
                               MARBLEBOARD_BEGIN_X, MARBLEBOARD_BEGIN_Y,
                               MARBLEBOARD_WALL_WIDTH, NORMAL_BOX_COLOR)
        self.leaderboard = LeaderBoard()       
        self.clickboard = Box(CLICKBOARD_HEIGHT, CLICKBOARD_LENGTH,
                              CLICKBOARD_BEGIN_X, CLICKBOARD_BEGIN_Y,
                              CLICKBOARD_WALL_WIDTH, NORMAL_BOX_COLOR)
        self.quitgif = Gif(QUIT_GIF_X, QUIT_GIF_Y, QUITGIF_FILENAME)
        self.xgif = Gif(X_BUTTON_GIF_X, X_BUTTON_GIF_Y, X_BUTTON_FILENAME)
        self.checkgif = Gif(CHECK_GIF_X, CHECK_GIF_Y, CHECK_BUTTON_FILENAME)
        self.check_button_position = Marble(Point(CHECK_BUTTON_POSITION_X,
                                                  CHECK_BUTTON_POSITION_Y),
                                            EMPTY_MARBLE_COLOR,
                                            size = CHECK_BUTTON_SIZE)
        self.x_button_position = Marble(Point(X_BUTTON_POSITION_X,
                                              X_BUTTON_POSITION_Y),
                                        EMPTY_MARBLE_COLOR, size=X_BUTTON_SIZE)
        self.row_marble_lst = []
        self.mini_group_lst = []
        self.color_marble_lst  = []

    def __str__(self):
        '''
        This method draws the gameboard
        instance on the screen.
        Parameters: None
        Return: None, the instance drawn
        '''
        self.marbleboard.__str__()
        self.leaderboard.__str__()
        self.clickboard.__str__()
        self.quitgif.__str__()
        self.xgif.__str__()
        self.checkgif.__str__()
        self.draw_marble_rows()
        self.draw_mini_marble_rows()
        self.draw_guessing_marbles()

    def __eq__(self, other):
        '''
        This method determines whether two
        GameBoard instances are equal.
        Parameters: other -- GameBoard instance
        Return: Boolean       
        '''
        return (self.marbleboard == other.marbleboard and 
                self.leaderboard == other.leaderboard and  
                self.clickboard == other.clickboard and 
                self.quitgif == other.quitgif and self.xgif == other.xgif and
                self.checkgif == other.checkgif and 
                self.check_button_position == other.check_button_position and 
                self.x_button_position == other.x_button_position and 
                self.row_marble_lst == other.row_marble_lst and 
                self.mini_group_lst == other.mini_group_lst and
                self.color_marble_lst == other.color_marble_lst)

    def draw_marble_rows(self):
        '''
        This method draws the 10 marbleboard
        rows of guessing marbles. It updates
        the list of guess marble instances.
        Parameters: None
        Return: None, the marble rows are drawn
        '''
        marble_guess_y = BEGIN_MARBLE_ROW_Y
        for i in range(NUMBER_MARBLE_ROWS):
            marble_guess_y = marble_guess_y - MARBLE_ROW_DISTANCE_Y
            marble_guess_x = BEGIN_MARBLE_ROW_X
            marble_lst = []
            for i in range(NUMBER_MARBLES_EACH_ROW):
                marble_guess_x = marble_guess_x + MARBLE_ROW_DISTANCE_X
                marble = Marble(Point(marble_guess_x,
                                      marble_guess_y), EMPTY_MARBLE_COLOR)
                marble_lst.append(marble)
                marble.draw_empty()
            self.row_marble_lst.append(marble_lst)

    def draw_mini_marble_rows(self):
        '''
        This method draws the 10 marbleboard
        rows of groups of mini peg marbles.
        It updates the list of mini marble group instances.
        Parameters: None
        Return: None, the mini peg marble groups are drawn
        '''
        mini_marble_y = BEGIN_MINI_MARBLE_ROW_Y
        for i in range(NUMBER_MINI_MARLBE_GROUPS):
            mini_marble_y = mini_marble_y - MINI_MARBLE_GROUP_DISTANCE_Y
            mini_marble_lst = []
            for i in range(NUMBER_IN_MINI_GROUP_TOP_ROW):
                mini_marble_y = mini_marble_y - MINI_MARBLE_DISTANCE_Y
                mini_marble_x = BEGIN_MINI_MARBLE_ROW_X
                for j in range(NUMBER_IN_MINI_GROUP_BOTTOM_ROW):
                    mini_marble_x = mini_marble_x + MINI_MARBLE_DISTANCE_X
                    mini_marble = Marble(Point(mini_marble_x, mini_marble_y),
                                         EMPTY_MARBLE_COLOR,
                                         size = MINI_MARBLE_SIZE)
                    mini_marble_lst.append(mini_marble)
                    mini_marble.draw_empty()
            self.mini_group_lst.append(mini_marble_lst)
        
    def draw_guessing_marbles(self):
        '''
        This method draws the clickboard
        row of colored marbles. It updates
        the list of colored marble instances.
        Parameters: None
        Return: None, the colored marbles are drawn
        '''
        color_marble_x = COLOR_MARBLES_BEGIN_X
        for i in range(len(COLORS)):
            color_marble_x = color_marble_x + COLOR_MARBLES_DISTANCE_X
            marble = Marble(Point(color_marble_x, COLOR_MARBLES_BEGIN_Y),
                            COLORS[i])
            self.color_marble_lst.append(marble)
            marble.draw()

            
