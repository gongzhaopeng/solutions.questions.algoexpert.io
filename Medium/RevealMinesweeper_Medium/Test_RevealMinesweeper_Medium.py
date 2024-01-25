# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_RevealMinesweeper_Medium as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        board = [
            ["H", "H", "H", "H", "M"],
            ["H", "1", "M", "H", "1"],
            ["H", "H", "H", "H", "H"],
            ["H", "H", "H", "H", "H"],
        ]
        row = 3
        column = 4
        expected = [
            ["0", "1", "H", "H", "M"],
            ["0", "1", "M", "2", "1"],
            ["0", "1", "1", "1", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        actual = program.revealMinesweeper(board, row, column)
        self.assertEqual(actual, expected)
