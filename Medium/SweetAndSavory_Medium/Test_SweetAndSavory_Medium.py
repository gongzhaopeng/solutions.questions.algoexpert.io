# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionII_SweetAndSavory_Medium as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        dishes = [-3, -5, 1, 7]
        target = 8
        expected = [-3, 7]
        actual = program.sweetAndSavory(dishes, target)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        dishes = [-5, 10]
        target = 5
        expected = [-5, 10]
        actual = program.sweetAndSavory(dishes, target)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        dishes = [17, 37, 12, -102, 53, 49, -90, 102, 49, 16, 52]
        target = -100
        expected = [0, 0]
        actual = program.sweetAndSavory(dishes, target)
        self.assertEqual(actual, expected)

    def test_case_4(self):
        dishes = [-3, -5, 1, 7]
        target = 0
        expected = [-3, 1]
        actual = program.sweetAndSavory(dishes, target)
        self.assertEqual(actual, expected)
