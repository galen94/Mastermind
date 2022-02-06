'''
Galen Otten
CS 5001, Spring 2021
Final Project: MasterMind
This file begins the game.
'''

import random
import turtle
from Marble import Marble
from Point import Point
from Gif import Gif
from Box import Box
from LeaderBoard import LeaderBoard
from GameBoard import GameBoard
from GameModel import GameModel
from GameView import GameView


def count_bulls_and_cows(secret_code, guess):
    '''
    This function compares the current guess
    to the secret code by counting how many colors
    were guessed correctly by the user
    both by color and position or just by color.
    Parameters: secret_code -- list, guess -- list
    Return: tuple: bulls -- int, cows -- int
    '''
    bulls = 0
    cows = 0
    for i in range(len(guess)):
        if guess[i] == secret_code[i]:
            bulls += 1
        elif guess[i] in secret_code:
            cows += 1
    return (bulls, cows)

def main():

    # set up the screen and user input box, initiate the GameView instance
    screen = turtle.Screen()
    game_view = GameView()

    # validate user's playername, display welcome message
    while (len(game_view.playername) == 0 or len(game_view.playername) > 10 or
           " " in game_view.playername):
        game_view.playername = turtle.textinput("CS 5001 MasterMind",
                                                "Please enter"
                                                " a name between 1 and 10"
                                                " characters long, no spaces: ")
        if len(game_view.playername) > 0 and len(game_view.playername) < 11:
            game_view.welcome_message = game_view.screen.title(("Welcome"
                                                                "to MasterMind " +
                                                                game_view.playername
                                                               + "!"))
    # display the GameView instance, begin the game
    game_view.__str__()
    screen.onclick(game_view.listen_to_clicks)
    
if __name__ == "__main__":
    main()
