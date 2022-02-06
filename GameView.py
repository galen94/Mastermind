'''
Galen Otten
CS 5001, Spring 2021
Final Project: MasterMind
This GameView class creates
the display of visual aspects
of the game.
'''

import turtle
import random
from Point import Point
from Marble import Marble
from Gif import Gif
from Box import Box
from LeaderBoard import LeaderBoard
from GameBoard import GameBoard
from GameModel import GameModel

LAST_ROW_INDEX_MARBLES = 9
ROW_MARKER_SIZE = 1
ROW_MARKER_BEGIN_X = -350
ROW_MARKER_BEGIN_Y = 275
ROW_MARKER_TURN_ANGLE = 90
ROW_MARKER_MOVE_DISTANCE = 45
ROW_MARKER_SHAPE = "turtle"
ROW_MARKER_COLOR = "green"
CENTER_GIF_DISPLAY_X = 0
CENTER_GIF_DISPLAY_Y = 0
SECRET_CODE_LENGTH = 4
QUIT_BOUNDARY_LEFT_X = 225
QUIT_BOUNDARY_RIGHT_X = 325
QUIT_BOUNDARY_UP_Y = -225
QUIT_BOUNDARY_DOWN_Y = -275
QUIT_MESSAGE = "quitmsg.gif"
BULLS_MARBLE_COLOR = "black"
COWS_MARBLE_COLOR = "red"
WINNER_MESSAGE = "winner.gif"
LOSER_MESSAGE = "Lose.gif"

class GameView:
    '''
    This GameView class sets up the gameboard and reacts
    to the user's input(clicks) accordingly.
    It includes methods that listen to the user's
    input, handle the clickable X, check and quit gifs,
    color a guess, give the user hints,
    and gives the winner or loser a final message.
    '''
    def __init__(self):
        '''
        This method creates an instance of a game view
        which has a gameboard, a player name,
        a personalized welcome message, a gamemodel,
        and a row marker turtle.
        Parameters: None
        Return: None, A game instance
        '''
        self.turbo = turtle.Turtle()
        self.screen = turtle.Screen()
        self.playername = turtle.textinput("CS 5001 MasterMind", "Your name,"
                                           " no spaces: ")
        if len(self.playername) > 0 and len(self.playername) < 11:
            self.welcome_message = self.screen.title(("Welcome to MasterMind "
                                                      + self.playername + "!"))
        self.board = GameBoard()
        self.gamemodel = GameModel()
        # self.flash is the green turtle working as the row marker
        self.flash = turtle.Turtle()
      
    def __str__(self):
        '''
        This method draws the gameboard
        and the row marker on the screen.
        Parameters: None
        Return: None, the visual game
        aspects drawn.
        '''
        self.turbo.hideturtle()
        self.board.__str__()
        self.set_up_row_marker()

    def __eq__(self, other):
        '''
        This method determines whether two
        GameView instances are equal.
        Parameters: other -- GameView instance
        Return: Boolean       
        '''
        return (self.playername == other.playername and
                self.welcome_message == other.welcome_message and 
                self.board == other.board and self.gamemodel == other.gamemodel)

    def set_up_row_marker(self):
        '''
        This method sets up the row marker
        on the screen, represented as
        the green turtle, Flash.
        Parameters: None
        Return: None, the green turtle set up
        '''
        self.flash.shape(ROW_MARKER_SHAPE)
        self.flash.color(ROW_MARKER_COLOR)
        self.flash.turtlesize(ROW_MARKER_SIZE)
        self.flash.penup()
        self.flash.goto(ROW_MARKER_BEGIN_X, ROW_MARKER_BEGIN_Y)
            
    def listen_to_clicks(self, x, y):
        '''
        This method waits for the user's clicks
        to decide which following instructions
        to follow. 
        Parameters: x -- float, y -- float
        Return: None
        '''
        self.handle_x_button(x, y)
        self.create_guess(x, y)
        self.handle_check_button(x, y)
        self.handle_quit_button(x, y)

    def handle_x_button(self, x, y):
        '''
        This method reacts to the click on the
        X button gif. It erases the current guess
        if it hasn't yet been checked. It then refills
        the colored marbles at the bottom. 
        Parameters: x -- float, y -- float
        Return: None
        '''
        if self.board.x_button_position.clicked_in_region(x, y):
            for each in self.board.row_marble_lst[self.gamemodel.row_marker]:
                each.draw_empty()
            self.gamemodel.temp_guess_lst.clear()
            self.gamemodel.guess.clear()
            for marble in self.board.color_marble_lst:
                marble.draw()
                            
    def handle_check_button(self, x, y):
        '''
        This method reacts to the click on the
        check button gif and handles the effects this action
        has on the game. It compares the current guess
        to the secret code, fills in the mini marbles to
        give the user a hint, refills the colored marbles
        at the bottom, and determines whether the user won,
        lost or should continue guessing. 
        Parameters: x -- float, y -- float
        Return: None
        '''
        if (self.board.check_button_position.clicked_in_region(x, y)  
            and len(self.gamemodel.guess) == SECRET_CODE_LENGTH):
            bulls, cows = self.gamemodel.count_bulls_and_cows()
            self.color_mini_pegs(bulls, cows)
            for marble in self.board.color_marble_lst:
                marble.draw()
            self.determine_win_lose_continue()
            
    def handle_quit_button(self, x, y):
        '''
        This method reacts to the click on the
        quit button gif. It ends the game and displays
        a quit message for the user to read. It
        exits the the screen when the user clicks anywhere.
        Parameters: x -- float, y -- float
        Return: None
        '''
        if ((x >= QUIT_BOUNDARY_LEFT_X and x <= QUIT_BOUNDARY_RIGHT_X)
            and (y <= QUIT_BOUNDARY_UP_Y and y >= QUIT_BOUNDARY_DOWN_Y)):
            quitter_gif = Gif(CENTER_GIF_DISPLAY_X,
                              CENTER_GIF_DISPLAY_Y, QUIT_MESSAGE)
            quitter_gif.__str__()
            turtle.exitonclick()
            
    def create_guess(self, x, y):
        '''
        This method reacts to a click on a
        colored marble in the clickboard. It fills
        in the marble based on the color of the colored marble,
        the current marble position and the current guess row.
        This click also causes an update to the guess list.
        Parameters: x -- float, y -- float
        Return: None, the guess list attribute is updated
        '''
        for marble in self.board.color_marble_lst:
            if marble.clicked_in_region(x, y):
                if len(self.gamemodel.temp_guess_lst) < SECRET_CODE_LENGTH:
                    color = marble.get_color()
                    if color not in self.gamemodel.temp_guess_lst:
                        self.gamemodel.marble_position = len(self.gamemodel.temp_guess_lst)
                        self.gamemodel.temp_guess_lst.append(color)
                        self.board.row_marble_lst[self.gamemodel.row_marker][self.gamemodel.marble_position].set_color(color)
                        self.board.row_marble_lst[self.gamemodel.row_marker][self.gamemodel.marble_position].draw()
                        marble.draw_empty() 
                        if len(self.gamemodel.temp_guess_lst) == SECRET_CODE_LENGTH:
                            for each in self.gamemodel.temp_guess_lst:
                                self.gamemodel.guess.append(each)

    def color_mini_pegs(self, bulls, cows):
        '''
        This method colors the mini peg marbles
        according to the user's guess. If the marble was
        both in the correct position and had the correct color,
        the mini marble will be black, and if the guess marble was
        just the right color, the mini marble will be red. If neither,
        the mini marble will be blank.
        Parameters: bulls -- int, cows -- int
        Return: None
        '''
        for i in range(bulls):
            self.board.mini_group_lst[self.gamemodel.row_marker][i].set_color(BULLS_MARBLE_COLOR)
            self.board.mini_group_lst[self.gamemodel.row_marker][i].draw()
        for j in range(cows):
            self.board.mini_group_lst[self.gamemodel.row_marker][j + bulls].set_color(COWS_MARBLE_COLOR)
            self.board.mini_group_lst[self.gamemodel.row_marker][j + bulls].draw()
            
    def determine_win_lose_continue(self):
        '''
        This method determines whether the user won,
        lost or should continue guessing. If they won
        or lost, the screen will display a message
        accordingly and the user will click anywhere to exit.
        If neither, the row marker will update and the
        guessing will continue.
        Parameters: None
        Return: None
        '''
        if self.gamemodel.guess == self.gamemodel.secret_code:
            self.update_leader_file()
            winner_gif = Gif(CENTER_GIF_DISPLAY_X,
                             CENTER_GIF_DISPLAY_Y, WINNER_MESSAGE)
            winner_gif.__str__() 
            turtle.exitonclick()     
        elif (self.gamemodel.guess != self.gamemodel.secret_code
              and self.gamemodel.row_marker == LAST_ROW_INDEX_MARBLES):
            loser_gif = Gif(CENTER_GIF_DISPLAY_X,
                            CENTER_GIF_DISPLAY_Y, LOSER_MESSAGE)
            loser_gif.__str__()
            turtle.exitonclick()
        else:
            self.move_to_next_guess()

    def move_to_next_guess(self):
        '''
        This method moves the row marker
        to the next guess row and clears
        the previous guess lists.
        Parameters: None
        Return: None
        '''
        self.flash.right(ROW_MARKER_TURN_ANGLE)
        self.flash.penup()
        self.flash.forward(ROW_MARKER_MOVE_DISTANCE)
        self.flash.left(ROW_MARKER_TURN_ANGLE)
        self.gamemodel.row_marker += 1
        self.gamemodel.temp_guess_lst.clear()
        self.gamemodel.guess.clear()

    def update_leader_file(self):
        '''
        test this method
        This method updates the leaderboard
        file with the player name and score
        if they won the game. If it's a new winner,
        then the file is appended to. If the winner
        is already in the file, but the score is better
        than their last, the score is updated. If there
        is no leaderboard file by the given file name, a
        new file is made with the winner and score.
        Parameters: None (It uses self.playername and
            self.board.leaderboard.file, but their values are
            reassigned here and passed into smaller functions
            in the GameModel class that can be tested without
            involving the attributes of the GameView constructor.)
        Return: Updated leaderboard file
        '''
        nested_leaders_lst = []
        updated_lst = []
        names_lst = []
        file_name = self.board.leaderboard.file
        player_name = self.playername
        number_of_guesses = self.gamemodel.determine_number_of_guesses()
        update = (number_of_guesses + "            " + player_name)
        try:
            self.gamemodel.read_leader_file(nested_leaders_lst, names_lst,
                                            file_name)
            if player_name not in names_lst:
                self.gamemodel.append_new_leader(update, file_name)
            else:
                self.gamemodel.update_old_leader_score(number_of_guesses, nested_leaders_lst, 
                                                       file_name, updated_lst, player_name)
        except:
            self.gamemodel.write_new_file(update, file_name)





