import unittest

from tictactoe import TicTacGame


class FinalsTestClass(unittest.TestCase):

    tests_map = [
        # draw
        ('Game over : Draw!', ['1', '2', '3', '5', '4', '7', '8', '6', '9']),
        # diagonal
        ('Game over : x is the winner!', ['1', '2', '5', '4', '9']),
        ('Game over : 0 is the winner!', ['2', '3', '4', '5', '8', '7']),
        # horizontal
        ('Game over : x is the winner!', ['1', '5', '2', '4', '3']),
        ('Game over : 0 is the winner!', ['2', '4', '1', '5', '8', '6']),
        ('Game over : x is the winner!', ['7', '2', '8', '4', '9']),
        # vertical
        ('Game over : 0 is the winner!', ['1', '2', '3', '5', '4', '8']),
        ('Game over : x is the winner!', ['1', '2', '4', '5', '7']),
        ('Game over : 0 is the winner!', ['1', '3', '8', '6', '4', '9'])
    ]

    def test_game(self):
        game = TicTacGame()
        for result, inp in self.tests_map:
            game.start_game()
            self.assertEqual(game.validate_game(inp), result)


class ExceptionsTestClass(unittest.TestCase):

    tests_map = [
        ('Error: Invalid cell number', ['10']),
        ('Error: Invalid cell number', ['0']),
        ('Error: Invalid cell number', ['-5']),
        ('Error: This cell is already taken', ['1', '1']),
        ('Error: Invalid input format', ['aaaaa']),
        ('Error: Invalid input format', [' '])
    ]

    def test_game(self):
        game = TicTacGame()
        for result, inp in self.tests_map:
            game.start_game()
            self.assertRaises(Exception, game.validate_game(inp), msg=result)


if __name__ == '__main__':
    unittest.main()
