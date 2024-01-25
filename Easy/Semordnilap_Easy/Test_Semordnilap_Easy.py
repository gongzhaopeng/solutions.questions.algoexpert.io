# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_Semordnilap_Easy as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = ["desserts", "stressed", "hello"]
        expected = [["desserts", "stressed"]]
        actual = program.semordnilap(input)
        self.assertEqual(actual, expected)
