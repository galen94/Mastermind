'''
Galen Otten
CS 5001, Spring 2021
Final Project: MasterMind
This LeaderBoard Class creates
a leaderboard to display and
read the highest scores and
associated player names.
'''

import turtle
import time
from Box import Box
from Gif import Gif

LEADERBOARD_HEIGHT = 485
LEADERBOARD_LENGTH = 250
LEADERBOARD_BEGIN_X = 100
LEADERBOARD_BEGIN_Y = 300
LEADERBOARD_WALL_WIDTH = 4
LEADERBOARD_WALL_COLOR = "blue"
LEADER_TITLE_X = 145
LEADER_TITLE_Y = 265
SCORE_TITLE_X = 115
SCORE_TITLE_Y = 225
LEADER_TITLE_FONT_SIZE = 20
SCORE_TITLE_FONT_SIZE = 16
SCORES_FONT_SIZE = 16
BEGIN_SCORES_X = 115
BEGIN_SCORES_Y = 210
SCORE_DISTANCE_Y = 40
CENTER_GIF_DISPLAY_X = 0
CENTER_GIF_DISPLAY_Y = 0
DISPLAY_ERROR_SECONDS = 3
MAXIMUM_LEADER_DISPLAY = 10
TURTLE_COLOR_SCORES = "green"
TURTLE_COLOR_TITLES = "black"
FONT_NAME = "Arial"
FONT_TYPE = "normal"
SCORE_ALIGNMENT = "left"
LEADERBOARD_ERROR_FILE_NAME = "leaderboard_error.gif"
LEADERBOARD_TITLE = "Leaderboard"
LEADERBOARD_SCORE_TITLE = "Score      Player"
LEADERBOARD_FILENAME = "leaderboard.txt"


class LeaderBoard:
    '''
    This Leaderboard class creates a
    leaderboard instance and describes the
    actions that can be done with this instance.
    These include drawing the borders, and
    writing the headers, the scores, and the
    leader names of the 10 highest scoring
    players written from best to worst scores.
    '''
    def __init__(self):
        '''
        This method creates an instance
        of a leaderboard using the given file.
        Parameters: leaderboard_file -- string file name
        Return: A leaderboard instance
        '''
        self.screen = turtle.Screen()
        self.turbo = turtle.Turtle()
        self.borders = Box(LEADERBOARD_HEIGHT, LEADERBOARD_LENGTH,
                           LEADERBOARD_BEGIN_X, LEADERBOARD_BEGIN_Y,
                           LEADERBOARD_WALL_WIDTH, LEADERBOARD_WALL_COLOR)
        self.file = LEADERBOARD_FILENAME
        self.title = LEADERBOARD_TITLE
        self.score_header = LEADERBOARD_SCORE_TITLE

    def __str__(self):
        '''
        This method draws the leaderboard
        instances on the screen.
        Parameters: None
        Return: None, the instance drawn
        '''
        self.borders.__str__()
        self.write_leader_headings()
        self.display_leaders()

    def __eq__(self, other):
        '''
        This method determines whether two
        LeaderBoard instances are equal.
        Parameters: other -- LeaderBoard instance
        Return: Boolean       
        '''
        return (self.borders == other.borders and self.file == other.file
                and self.title == other.title
                and self.score_header == other.score_header)

    def write_leader_headings(self):
        '''
        This method writes the titles
        "Leaderboard", and "Score    Player"
        on the screen.
        Parameters: None
        Return: None, the titles written
        '''
        self.turbo.up()
        self.turbo.goto(LEADER_TITLE_X, LEADER_TITLE_Y)
        self.turbo.color(TURTLE_COLOR_TITLES)
        self.turbo.write(self.title, True, align = SCORE_ALIGNMENT,
                         font = (FONT_NAME, LEADER_TITLE_FONT_SIZE, FONT_TYPE))
        self.turbo.goto(SCORE_TITLE_X, SCORE_TITLE_Y)
        self.turbo.color(TURTLE_COLOR_TITLES)
        self.turbo.write(self.score_header, True, align = SCORE_ALIGNMENT,
                         font = (FONT_NAME, SCORE_TITLE_FONT_SIZE, FONT_TYPE))

    def display_leaders(self):
        '''
        This method attempts to read the file
        and write the(at most 10) highest scores and
        associated names on the screen. If
        there is no such file, an error
        message will appear and no scores or
        names will be written on the leaderboard.
        If there is another problem with the file,
        the game will end.
        Parameters: None
        Return: None, the scores/names written
        '''
        try:
            leaders = self.read_sort_leader_file()
            self.write_names_scores(leaders)
        except FileNotFoundError:
            self.display_error(LEADERBOARD_ERROR_FILE_NAME)
        except OSError as err:   
            print("OS error: {}".format(err))
            print("Something went wrong. Goodbye.")
            turtle.done()

    def read_sort_leader_file(self):
        '''
        This method opens and reads the leader file,
        then sorts the lines by best scores. This
        method is tested in the Test Suite.
        Parameters: None
        Return: leaders -- sorted list
        '''
        with open(self.file, "r") as file:
            leaders = file.readlines()
            leaders.sort()
        return leaders

    def write_names_scores(self, leaders):
        '''
        This method writes the scores and names
        on the leaderboard according to the sorted
        lists "leaders". 
        Parameters: leaders -- sorted list
        Return: None, the scores and leaders written
            on the screen
        '''
        y = BEGIN_SCORES_Y
        self.turbo.color(TURTLE_COLOR_SCORES)
        if len(leaders) < MAXIMUM_LEADER_DISPLAY:
            for i in range(len(leaders)):
                y = y - SCORE_DISTANCE_Y
                self.turbo.goto(BEGIN_SCORES_X, y)
                self.turbo.write(leaders[i], align = SCORE_ALIGNMENT,
                                 font = (FONT_NAME, SCORES_FONT_SIZE, FONT_TYPE))                
        else:
            for i in range(MAXIMUM_LEADER_DISPLAY):
                y = y - SCORE_DISTANCE_Y
                self.turbo.goto(BEGIN_SCORES_X, y)
                self.turbo.write(leaders[i], align = SCORE_ALIGNMENT,
                                 font = (FONT_NAME, SCORES_FONT_SIZE, FONT_TYPE))               
        self.turbo.hideturtle()
        
    def display_error(self, error):
        '''
        This method displays an error
        message while pausing the game
        for 3 seconds so that the user can
        read it.
        Parameters: error -- string file name
        '''
        self.screen.addshape(error)
        self.turbo.up()
        self.turbo.goto(CENTER_GIF_DISPLAY_X, CENTER_GIF_DISPLAY_Y)
        self.turbo.shape(error)
        time.sleep(DISPLAY_ERROR_SECONDS)
        self.turbo.hideturtle()

        
