# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionII_DiceThrows_Hard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        numDice = 2
        numSides = 6
        target = 7
        expected = 6
        actual = program.diceThrows(numDice, numSides, target)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        numDice = 1
        numSides = 6
        target = 7
        expected = 0
        actual = program.diceThrows(numDice, numSides, target)
        self.assertEqual(actual, expected)
