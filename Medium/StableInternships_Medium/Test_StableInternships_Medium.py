# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_StableInternships_Medium as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        interns = [[0, 1], [1, 0]]
        teams = [[1, 0], [1, 0]]
        expected = [[0, 0], [1, 1]]
        actual = program.stableInternships(interns, teams)
        self.assertTrue(len(actual) == len(expected))

        for match in expected:
            containsMatch = False
            for actualMatch in actual:
                if actualMatch[0] == match[0] and actualMatch[1] == match[1]:
                    containsMatch = True
            self.assertTrue(containsMatch)
