# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_LevenshteinDistance_Medium as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.levenshteinDistance("abc", "yabd"), 2)

    def test_case_2(self):
        self.assertEqual(program.levenshteinDistance("", "abc"), 3)
