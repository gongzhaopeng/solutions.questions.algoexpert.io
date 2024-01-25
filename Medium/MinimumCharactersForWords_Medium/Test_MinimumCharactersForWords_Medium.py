# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionII_MinimumCharactersForWords_Medium as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = ["this", "that", "did", "deed", "them!", "a"]
        expected = ["t", "t", "h", "i", "s", "a", "d", "d", "e", "e", "m", "!"]
        actual = program.minimumCharactersForWords(input)
        self.assertCountEqual(actual, expected)
