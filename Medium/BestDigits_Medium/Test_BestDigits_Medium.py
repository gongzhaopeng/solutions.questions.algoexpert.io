# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionII_BestDigits_Medium as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        number = "462839"
        numDigits = 2
        expected = "6839"
        actual = program.bestDigits(number, numDigits)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        number = "22"
        numDigits = 1
        expected = "2"
        actual = program.bestDigits(number, numDigits)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        number = "12345"
        numDigits = 0
        expected = "12345"
        actual = program.bestDigits(number, numDigits)
        self.assertEqual(actual, expected)
