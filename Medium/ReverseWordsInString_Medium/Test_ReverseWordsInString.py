# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionIII_ReverseWordsInString_Medium as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = "AlgoExpert is the best!"
        expected = "best! the is AlgoExpert"
        actual = program.reverseWordsInString(input)
        self.assertEqual(actual, expected)
