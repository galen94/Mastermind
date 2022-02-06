'''
Galen Otten
CS 5001, Spring 2021
The file creates a class to test
the non-turtle GameModel and
LeaderBoard class methods from
the MasterMind project.
'''

from LeaderBoard import LeaderBoard
from GameModel import GameModel
import unittest

class TestMasterMind(unittest.TestCase):
    '''
    This test class tests the non-turtle methods 
    from the GameModel and LeaderBoard classes.
    '''    
    def get_file_contents(self):
        '''
        This method helps to test the method below:
        test_read_sort_leader_file()
        '''
        contents = ["1            tutu\n", "3            google\n"]
        return contents

    def get_bad_file_contents(self):
        '''
        This method helps to test the method below:
        test_read_sort_leader_file()
        '''
        bad_contents = ["3            google\n, 1            tutu\n"]
        return bad_contents
       
    def test_read_sort_leader_file(self):
        '''
        This method and the two methods
        (get_file_contents(), get_bad_file_contents())
        test the method read_sort_leader_file() from
        the Leaderboard class. It tests that the leaders
        and scores are sorted properly after the file
        is opened and read. The file "leaterdoard.txt" is
        included in the final project file because it has
        specific contents to test this file.
        '''
        leaderboard = LeaderBoard()
        leaderboard.file = "test_read_sort_leader_file.txt"
        self.assertEqual(leaderboard.read_sort_leader_file(),
                         self.get_file_contents())
        self.assertNotEqual(leaderboard.read_sort_leader_file(),
                         self.get_bad_file_contents())


    def test__init__(self):
        '''
        This tests the constructor
        of the GameModel class.
        '''
        gamemodel = GameModel()
        
        self.assertEqual(type(gamemodel.secret_code), list)
        self.assertEqual(len(gamemodel.secret_code), 4)
        self.assertNotEqual(type(gamemodel.secret_code), str)
        self.assertNotEqual(type(gamemodel.secret_code), dict)
        self.assertNotEqual(type(gamemodel.secret_code), set)
        self.assertNotEqual(type(gamemodel.secret_code), int)
        self.assertNotEqual(type(gamemodel.secret_code), float)
        self.assertAlmostEqual(len(gamemodel.secret_code), 4.0)
        self.assertNotEqual(len(gamemodel.secret_code), "4")
        self.assertNotEqual(len(gamemodel.secret_code), -4)
        
        self.assertEqual(type(gamemodel.guess), list)
        self.assertEqual(len(gamemodel.guess), 0)
        self.assertNotEqual(type(gamemodel.guess), str)
        self.assertNotEqual(type(gamemodel.guess), dict)
        self.assertNotEqual(type(gamemodel.guess), int)
        self.assertNotEqual(type(gamemodel.guess), set)
        self.assertNotEqual(len(gamemodel.guess), "0")
        self.assertNotEqual(len(gamemodel.guess), 1)

        self.assertEqual(type(gamemodel.temp_guess_lst), list)
        self.assertEqual(len(gamemodel.temp_guess_lst), 0)
        self.assertNotEqual(type(gamemodel.temp_guess_lst), str)
        self.assertNotEqual(type(gamemodel.temp_guess_lst), dict)
        self.assertNotEqual(type(gamemodel.temp_guess_lst), int)
        self.assertNotEqual(type(gamemodel.temp_guess_lst), set)
        self.assertNotEqual(len(gamemodel.temp_guess_lst), "0")
        self.assertNotEqual(len(gamemodel.temp_guess_lst), 1)

        self.assertEqual(type(gamemodel.row_marker), int)
        self.assertEqual(gamemodel.row_marker, 0)
        self.assertAlmostEqual(gamemodel.row_marker, 0.0)
        self.assertNotEqual(type(gamemodel.row_marker), str)
        self.assertNotEqual(type(gamemodel.row_marker), float)
        self.assertNotEqual(type(gamemodel.row_marker), list)
        self.assertNotEqual(type(gamemodel.row_marker), set)
        self.assertNotEqual(gamemodel.row_marker, "0")
        self.assertNotEqual(gamemodel.row_marker, 1)

        self.assertEqual(type(gamemodel.marble_position), int)
        self.assertEqual(gamemodel.marble_position, 0)
        self.assertAlmostEqual(gamemodel.marble_position, 0.0)
        self.assertNotEqual(type(gamemodel.marble_position), str)
        self.assertNotEqual(type(gamemodel.marble_position), float)
        self.assertNotEqual(type(gamemodel.marble_position), list)
        self.assertNotEqual(type(gamemodel.marble_position), set)
        self.assertNotEqual(gamemodel.marble_position, "0")
        self.assertNotEqual(gamemodel.marble_position, 1)

    def test__str__(self):
        '''
        This tests the __str__ method
        of the GameModel class.
        '''
        gamemodel = GameModel()
        
        gamemodel.secret_code = ["blue", "green", "yellow", "purple"]
        self.assertEqual(gamemodel.__str__(),
                         ["blue", "green", "yellow", "purple"])
        self.assertNotEqual(gamemodel.__str__(),
                            "blue, green, yellow, purple")
        self.assertNotEqual(gamemodel.__str__(),
                            ["blue, green, yellow, purple"])
        self.assertNotEqual(gamemodel.__str__(),
                            {"blue", "green", "yellow", "purple"})
        self.assertNotEqual(gamemodel.__str__(),
                            ("blue", "green", "yellow", "purple"))

    def test__eq__(self):
        '''
        This tests the __eq__ method
        of the GameModel class.
        '''
        gamemodel = GameModel()
        gamemodel2 = GameModel()
        gamemodel3 = GameModel()
        gamemodel.secret_code = ["blue", "green", "yellow", "purple"]
        gamemodel2.secret_code = ["blue", "green", "yellow", "purple"]
        gamemodel3.secret_code = ["black", "green", "yellow", "purple"]
        self.assertTrue(gamemodel.__eq__(gamemodel2))
        self.assertFalse(gamemodel.__eq__(gamemodel3))
        
    
    def test_generate_secret_code(self):
        '''
        This tests the generate_secret_code()
        method of the GameModel class.
        '''
        gamemodel = GameModel()
        
        self.assertEqual(type(gamemodel.generate_secret_code()), list)
        self.assertNotEqual(type(gamemodel.generate_secret_code()), str)
        self.assertNotEqual(type(gamemodel.generate_secret_code()), dict)
        self.assertNotEqual(type(gamemodel.generate_secret_code()), set)
        self.assertNotEqual(type(gamemodel.generate_secret_code()), int)
        self.assertNotEqual(type(gamemodel.generate_secret_code()), float)
        self.assertNotEqual(type(gamemodel.generate_secret_code()), True)
        self.assertNotEqual(type(gamemodel.generate_secret_code()), False)
        
        self.assertEqual(len(gamemodel.generate_secret_code()), 4)
        self.assertAlmostEqual(len(gamemodel.generate_secret_code()), 4.0)
        self.assertNotEqual(len(gamemodel.generate_secret_code()), "4")
        self.assertNotEqual(len(gamemodel.generate_secret_code()), 3)
        self.assertNotEqual(len(gamemodel.generate_secret_code()), 2)
        self.assertNotEqual(len(gamemodel.generate_secret_code()), 1)
        self.assertNotEqual(len(gamemodel.generate_secret_code()), 0)
        self.assertNotEqual(len(gamemodel.generate_secret_code()), -4)
        self.assertNotEqual(len(gamemodel.generate_secret_code()), " 4 ")
        self.assertNotEqual(len(gamemodel.generate_secret_code()), (str(4)))
        self.assertNotEqual(len(gamemodel.generate_secret_code()), .4)
        
        self.assertEqual(type(gamemodel.generate_secret_code()[0]), str)
        self.assertEqual(type(gamemodel.generate_secret_code()[1]), str)
        self.assertEqual(type(gamemodel.generate_secret_code()[2]), str)
        self.assertEqual(type(gamemodel.generate_secret_code()[3]), str)
        self.assertNotEqual(type(gamemodel.generate_secret_code()[0]), list)
        self.assertNotEqual(type(gamemodel.generate_secret_code()[1]), dict)
        self.assertNotEqual(type(gamemodel.generate_secret_code()[2]), int)
        self.assertNotEqual(type(gamemodel.generate_secret_code()[3]), float)
                
    def test_count_bulls_and_cows(self):
        '''
        This tests the count_bulls_and_cows()
        method of the GameModel class.
        '''
        gamemodel = GameModel()
        
        gamemodel.secret_code = ["blue", "green", "yellow", "purple"]
        gamemodel.guess = ["blue", "green", "yellow", "purple"]
        self.assertEqual(gamemodel.count_bulls_and_cows(), (4, 0))
        
        gamemodel.secret_code = ["red", "green", "yellow", "purple"]
        gamemodel.guess = ["blue", "green", "yellow", "purple"]
        self.assertEqual(gamemodel.count_bulls_and_cows(), (3, 0))

        gamemodel.secret_code = ["red", "blue", "purple", "black"]
        gamemodel.guess = ["blue", "green", "yellow", "purple"]
        self.assertEqual(gamemodel.count_bulls_and_cows(), (0, 2))

        gamemodel.secret_code = ["black", "green", "purple", "yellow"]
        gamemodel.guess = ["blue", "green", "yellow", "purple"]
        self.assertEqual(gamemodel.count_bulls_and_cows(), (1, 2))
        gamemodel.guess = ["black", "green", "blue", "purple"]
        self.assertEqual(gamemodel.count_bulls_and_cows(), (2, 1))
        gamemodel.guess = ["black", "green", "yellow", "purple"]
        self.assertEqual(gamemodel.count_bulls_and_cows(), (2, 2))
        gamemodel.guess = ["green", "black", "yellow", "blue"]
        self.assertEqual(gamemodel.count_bulls_and_cows(), (0, 3))
        gamemodel.guess = ["green", "black", "yellow", "purple"]
        self.assertEqual(gamemodel.count_bulls_and_cows(), (0, 4))
    
    def test_read_leader_file(self):
        '''
        This method tests that the leaderboard file
        is read properly and correctly made into
        nested lists to access specific data.
        **The file "test_read_leader_file.txt" is included
        in the final project file because it has
        specific contents to test this file.
        ''' 
        
        gamemodel = GameModel()
        nested_leaders_lst = []
        names_lst = []
        file_name = "test_read_leader_file.txt"
        file_lsts = ([["3", "", "", "", "", "", "",
                      "", "", "", "", "", "Paolo"],
                     ["4", "", "", "", "", "", "",
                      "", "", "", "", "", "Jess"]],
                     ["Paolo", "Jess"])                     
        self.assertEqual(gamemodel.read_leader_file(nested_leaders_lst,
                                                    names_lst, file_name),
                         file_lsts)
                                                   
    def get_file_append_contents(self):
        '''
        This method helps to test the method below:
        test_append_new_leader()
        '''
        gamemodel = GameModel()
        update = "Hello Player!"
        file_name = "test_append_file.txt"
        gamemodel.append_new_leader(update, file_name)
        with open(file_name, "r") as file:
            contents = file.readlines()
            return contents
    
    def test_append_new_leader(self):
        '''
        This method and the get_file_append_contents()
        method test that the new leader and score are 
        properly added to the leaderboard file.
        **The file "test_append_file.txt" is included in the final
        project file because it has specific contents
        to test this file.        
        '''
        gamemodel = GameModel()
        file_name = "test_append_file.txt"
        self.assertEqual(self.get_file_append_contents()[-1],
                         "Hello Player!\n")
        self.assertNotEqual(self.get_file_append_contents()[-1],
                            "Hello Player!")
        self.assertNotEqual(self.get_file_append_contents(),
                            "Hello Player!")
    
    def get_file_update_contents(self):
        '''
        This method helps to test the method below:
        test_update_old_leader_score()
        '''
        gamemodel = GameModel()
        updated_lst = []
        file_name = "test_update_leader_file.txt"
        nested_leaders_lst = [["3", "", "", "", "", "", "",
                               "", "", "", "", "", "Paolo"],
                              ["4", "", "", "", "", "", "", "",
                               "", "", "", "", "Jess"]]
        player_name = "Jess"
        number_of_guesses = "2"
        expected_change = "3            Paolo\n2            Jess\n"
        gamemodel.update_old_leader_score(number_of_guesses,
                                          nested_leaders_lst, file_name,
                                          updated_lst, player_name)
        with open(file_name, "r") as file:
            contents = file.read()
            return contents
        
    def test_update_old_leader_score(self):
        '''
        This method and the get_file_update_contents()
        method test that the old leader's score is 
        properly updated in the leaderboard file.
        *The file "test_update_leader_file.txt"
        is included in the final project file
        because it has specific contents
        to test this file.        
        '''
        expected_change = "3            Paolo\n2            Jess\n"
        unexpected = "3            Paolo\n4            Jess\n"
        self.assertEqual(self.get_file_update_contents(), expected_change)
        self.assertNotEqual(self.get_file_update_contents(), unexpected) 

    def get_file_write_contents(self):
        '''
        This method helps to test the method below:
        test_write_new_file()
        '''
        gamemodel = GameModel()
        update = "Hello Turtle!"
        file_name = "test_write_files.txt"
        gamemodel.write_new_file(update, file_name)
        with open(file_name, "r") as file:
            contents = file.read()
            return contents
        
    def test_write_new_file(self):
        '''
        This method and the get_file_write_contents()
        method test that a new leaderboard file is
        created if there isn't one so far. 
        *The file "test_write_files.txt"
        is included in the final project file
        because it has specific contents
        to test this file.        
        '''
        self.assertEqual(self.get_file_write_contents(),
                         "Hello Turtle!\n")
        self.assertNotEqual(self.get_file_write_contents(),
                            "Hello Turtle!")

    def test_determine_number_of_guesses(self):
        '''
        This tests the determine_number_of_guesses()
        method of the GameModel class.
        '''
        gamemodel = GameModel()
        gamemodel.row_marker = 5
        self.assertEqual(gamemodel.determine_number_of_guesses(), "06")
        self.assertNotEqual(gamemodel.determine_number_of_guesses(), "05")
        self.assertNotEqual(gamemodel.determine_number_of_guesses(), "6")
        self.assertNotEqual(gamemodel.determine_number_of_guesses(), 0.6)
        self.assertNotEqual(gamemodel.determine_number_of_guesses(), 6)
        self.assertNotEqual(gamemodel.determine_number_of_guesses(), -6)
        
        gamemodel.row_marker = 9
        self.assertEqual(gamemodel.determine_number_of_guesses(), "10")
        self.assertNotEqual(gamemodel.determine_number_of_guesses(), "01")
        self.assertNotEqual(gamemodel.determine_number_of_guesses(), "1")
        self.assertNotEqual(gamemodel.determine_number_of_guesses(), 1.0)
        self.assertNotEqual(gamemodel.determine_number_of_guesses(), 10)
        self.assertNotEqual(gamemodel.determine_number_of_guesses(), -10)
        self.assertNotEqual(gamemodel.determine_number_of_guesses(), ".10")
        self.assertNotEqual(gamemodel.determine_number_of_guesses(), "100")

        gamemodel.row_marker = 0
        self.assertEqual(gamemodel.determine_number_of_guesses(), "01")
        self.assertNotEqual(gamemodel.determine_number_of_guesses(), "1")
        self.assertNotEqual(gamemodel.determine_number_of_guesses(), "0")
        self.assertNotEqual(gamemodel.determine_number_of_guesses(), "00")
        self.assertNotEqual(gamemodel.determine_number_of_guesses(), 1)
        self.assertNotEqual(gamemodel.determine_number_of_guesses(), 1.0)
        self.assertNotEqual(gamemodel.determine_number_of_guesses(), -1)
        self.assertNotEqual(gamemodel.determine_number_of_guesses(), "10")
        self.assertNotEqual(gamemodel.determine_number_of_guesses(), "001")

        gamemodel.row_marker = 1
        self.assertEqual(gamemodel.determine_number_of_guesses(), "02")
        self.assertNotEqual(gamemodel.determine_number_of_guesses(), "2")
        self.assertNotEqual(gamemodel.determine_number_of_guesses(), "1")
        self.assertNotEqual(gamemodel.determine_number_of_guesses(), "01")
        self.assertNotEqual(gamemodel.determine_number_of_guesses(), 2)
        self.assertNotEqual(gamemodel.determine_number_of_guesses(), 2.0)
        self.assertNotEqual(gamemodel.determine_number_of_guesses(), -2)
        self.assertNotEqual(gamemodel.determine_number_of_guesses(), "20")
        self.assertNotEqual(gamemodel.determine_number_of_guesses(), "002")
        
        

def main():
    
    unittest.main(verbosity = 3)

main()
        
