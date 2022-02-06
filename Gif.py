'''
Galen Otten
CS 5001, Spring 2021
Final Project: MasterMind
--Gif Class for messages and
clickable buttons--
'''

import turtle

class Gif:
    '''
    This Gif Class creates gifs
    for clicking on and making
    notes for the user to read. 
    '''
    def __init__(self, x, y, file_name):
        '''
        This method creates instances
        of gifs using the given location
        and filename.
        Parameters: x -- float, y -- float,
            file_name -- string name of gif file
        Return: A gif instance
        '''
        self.x = x
        self.y = y
        self.file_name = file_name
        self.screen = turtle.Screen()
        self.turbo = turtle.Turtle()

    def __str__(self):
        '''
        This method displays the gif instances
        on the screen.
        Parameters: None
        Return: None, the instance displayed
        '''
        self.screen.addshape(self.file_name)
        self.turbo.up()
        self.turbo.goto(self.x, self.y)
        self.turbo.shape(self.file_name)

    def __eq__(self, other):
        '''
        This method determines whether two Gif
        instances are equal.
        Parameters: other -- Gif instance
        Return: Boolean       
        '''
        return (self.file_name == other.filename
                and self.x == other.x and self.y == other.y) 
        





        
