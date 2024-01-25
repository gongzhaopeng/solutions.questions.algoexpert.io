# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_CollidingAsteroids_Medium as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [-3, 5, -8, 6, 7, -4, -7]
        expected = [-3, -8, 6]
        actual = program.collidingAsteroids(input)
        self.assertEqual(actual, expected)
