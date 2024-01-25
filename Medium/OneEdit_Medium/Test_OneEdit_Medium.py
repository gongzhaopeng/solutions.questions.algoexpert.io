# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_OneEdit_Medium as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        stringOne = "hello"
        stringTwo = "helo"
        expected = True
        actual = program.oneEdit(stringOne, stringTwo)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        stringOne = "a"
        stringTwo = "b"
        expected = True
        actual = program.oneEdit(stringOne, stringTwo)
        self.assertEqual(actual, expected)
