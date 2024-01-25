# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_TaskAssignment_Medium as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        k = 3
        tasks = [1, 3, 5, 3, 1, 4]
        expected = [[0, 2], [4, 5], [1, 3]]
        actual = program.taskAssignment(k, tasks)
        self.assertEqual(actual, expected)
