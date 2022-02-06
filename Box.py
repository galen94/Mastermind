'''
Galen Otten
CS 5001, Spring 2021
Final Project: MasterMind
This Box Class creates box
objects for the gameboard.
It is used to make the borders
for the marbleboard, leaderboard,
and clickboard.
'''
import turtle

SPEED = 0
BOX_ANGLE = 90

class Box:
    '''
    This Box Class creates
    boxes/boards to show
    different areas of the gameboard. 
    '''
    def __init__(self, height, length, x, y, wall_width, color):
        '''
        This method creates instances
        of boxes using the given location,
        dimensions, and color.
        Parameters: height -- float, length -- float,
            x -- float, y -- float, wall_width -- float,
            color -- string
        Return: A box instance
        '''
        self.height = height
        self.length = length
        self.x = x
        self.y = y
        self.wall_width = wall_width
        self.color = color
        self.turbo = turtle.Turtle()

    def __str__(self):
        '''
        This method draws the box instances
        on the screen.
        Parameters: None
        Return: None, the instance displayed
        '''
        self.turbo.up()
        self.turbo.goto(self.x, self.y)
        self.turbo.down()
        self.turbo.width(self.wall_width)
        self.turbo.pencolor(self.color)
        self.turbo.speed(SPEED)
        for i in range(2):
            self.turbo.forward(self.length)
            self.turbo.right(BOX_ANGLE)
            self.turbo.forward(self.height)
            self.turbo.right(BOX_ANGLE)
        self.turbo.hideturtle()

    def __eq__(self, other):
        '''
        This method determines whether two Box
        instances are equal.
        Parameters: other -- Box instance
        Return: Boolean       
        '''
        return (self.height == other.height and self.length == other.length
                and self.x == other.x and self.y == other.y
                and self.wall_width == other.wall_width
                and self.color == other.color)



        
