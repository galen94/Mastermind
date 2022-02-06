'''
Galen Otten
CS 5001, Spring 2021
Final Project: MasterMind
This GameModel class works
behind the scenes to initiate
a secret code and determine
the guess scores.
'''

import random

SECRET_CODE_LENGTH = 4
LAST_ROW_NUMBER = 9
LAST_ROW_SCORE = "10"
LEADING_ZERO = "0"

class GameModel:
    def __init__(self):
        '''
        This method creates an instance
        of a game model which has a row marker,
        a secret code, the user's guess and temporary guess, the
        number of guesses a user has taken so far,
        the row marker's position, and the current marble position.
        Parameters: None
        Return: None, A game model instance
        '''
        self.secret_code = self.generate_secret_code()
        self.guess = []
        self.temp_guess_lst = []
        self.row_marker = 0
        self.marble_position = 0

    def __str__(self):
        '''
        This method determines what
        would be printed for a human
        to be able to read this instance.
        Parameters: None
        Return: self.secret_code -- list
        '''
        return self.secret_code

    def __eq__(self, other):
        '''
        This method determines whether two
        GameModel instances are equal.
        Parameters: other -- GameModel instance
        Return: Boolean       
        '''
        return self.secret_code == other.secret_code
        
    def generate_secret_code(self):
        '''
        test this method
        This method generates a random list
        of 4 colors based on the colors list.
        Parameters: None
        Return: secret_code -- list of color strings
        '''
        colors = ["red", "blue", "green", "yellow", "purple", "black"]
        secret_code = []    
        for i in range(SECRET_CODE_LENGTH):
            marble_color = random.choice(colors)
            secret_code.append(marble_color)
            colors.remove(marble_color)
        return secret_code

    def count_bulls_and_cows(self):
        '''
        test this method
        This method compares the current guess
        to the secret code by counting how many colors
        were guessed correctly by the user
        both by color and position or just by color.
        Parameters: None
        Return: tuple: bulls -- int, cows -- int
        '''
        bulls = 0
        cows = 0
        for i in range(len(self.guess)):
            if self.guess[i] == self.secret_code[i]:
                bulls += 1
            elif self.guess[i] in self.secret_code:
                cows += 1
        return (bulls, cows)

    def read_leader_file(self, nested_leaders_lst, names_lst, file_name):
        '''
        This method opens the leaderboard file,
        and makes lists of leaders and scores to
        manipulate.
        Parameters: nested_leaders_lst -- list, names_lst -- list
        Return: updated lists of leaders and scores
            in the larger function             
        '''
        with open(file_name, "r") as file:
            leaders_lst = file.readlines()     
            for i in range(len(leaders_lst)):
                leaders_lst[i] = leaders_lst[i].replace("\n", "")
                nested_leaders_lst.append(leaders_lst[i].split(" "))
            for each in nested_leaders_lst:
                names_lst.append(each[12])
        return nested_leaders_lst, names_lst

    def append_new_leader(self, update, file_name):
        '''
        This method opens the leaderboard file
        and appends the new winner and score.
        Parameters: update -- string of name and score
        Return: Updated leaderboard file  
        '''
        with open(file_name, "a") as updated_file:
            updated_file.write(update)
            updated_file.write("\n")

    def update_old_leader_score(self, number_of_guesses, nested_leaders_lst,
                                file_name, updated_lst, player_name):
        '''
        This method opens the leaderboard file
        and updates with the old winner's new score.
        Parameters: nested_leaders_lst -- list,
            number_of_guesses -- string, updated_lst -- list
        Return: Updated leaderboard file 
        '''
        for each in nested_leaders_lst:
            if player_name == each[12]:
                if int(number_of_guesses) < int(each[0]):
                    each[0] = number_of_guesses
            string_each = " ".join(each)
            updated_lst.append(string_each)
        with open(file_name, "w") as updated_file:
            for leader in updated_lst:
                updated_file.write(leader)
                updated_file.write("\n")    
                
    def write_new_file(self, update, file_name):
        '''
        This method creates a new leaderboard
        file with the winner and score.
        Parameters: update -- string of name and score
        Return: A new leaderboard file 
        '''
        with open(file_name, "w") as updated_file:
            updated_file.write(update)
            updated_file.write("\n")

    def determine_number_of_guesses(self):
        if self.row_marker == LAST_ROW_NUMBER:
            number_of_guesses = LAST_ROW_SCORE
        else:
            number_of_guesses = LEADING_ZERO + str(self.row_marker + 1)
        return number_of_guesses


