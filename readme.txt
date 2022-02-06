'''
Galen Otten, Final Project
CS 5001, Spring 2021
My Mastermind explained
'''

    Thank you for playing my version of MasterMind! I decided to stick with the
original idea and not go for any extra credit at this point. So, it should
have one round per run of mastermind_game.py, with four unique colors in the
secret code. The leaderboard should display at most ten leaders with the
highest scores recorded. If a leader gets knocked off the display board, they
will still be in the leaderboard file, so they can climb back up if they beat
a player currently on the board.

    The way I structured my code design was with classes. I used
several small classes such as the Gif, Box, Marble, Point classes,
a LeaderBoard class that imports both my Gif and Box classes, a GameBoard
class that imports the Gif, Box, Marble, Point, and LeaderBoard classes, 
a GameModel class that only imports the random module and no other classes
because this class has no turtle/view affecting it. Finally, I have
a GameView class that imports all previously mentioned classes to
bring together every aspect of the game.

    I included a few txt files that the Test Suite needs in order to pass
the tests regarding the testing of file methods. These include:
    "test_read_sort_leader_file.txt"
    "test_read_leader_file.txt"
    "test_append_file.txt"
    "test_update_leader_file.txt"
    "test_write_files.txt"
    
