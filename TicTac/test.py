import unittest
from unittest.mock import patch
import io
import sys

from tictactoe import TicTacGame


class FirstTestClass(unittest.TestCase):

    tests_map = {
        'Game over : Draw!': ['1', '2', '3', '5', '4', '7', '8', '6', '9'],
        'Game over : x is the winner!': ['1', '2', '5', '4', '9'],
        'Game over : 0 is the winner!': ['1', '2', '3', '5', '4', '8']
    }

    def test_game(self):
        game = TicTacGame()
        for result, user_input in self.tests_map.items():
            game.start_game()
            with patch('builtins.input', side_effect=user_input):
                winner = None
                while not winner:
                    game.make_move()
                    winner = game.check_winner()
                self.assertEqual(winner, result)


class SecondTestClass(unittest.TestCase):

    tests_map = {
        'Error: Invalid cell number': ['5', '10', '2'],
        'Error: This cell is already taken': ['1', '1', '2'],
        'Error: Invalid input format': ['5', 'aaaaa', '1']
    }

    def test_bad_input(self):
        game = TicTacGame()
        for message, user_input in self.tests_map.items():
            game.start_game()
            with patch('builtins.input', side_effect=user_input):
                game.make_move()
                # to save output
                my_out = io.StringIO()
                sys.stdout = my_out
                game.make_move()
                sys.stdout = sys.__stdout__
                out_list = my_out.getvalue().split('\n')
                self.assertEqual(out_list[1], message)


if __name__ == '__main__':
    unittest.main()
