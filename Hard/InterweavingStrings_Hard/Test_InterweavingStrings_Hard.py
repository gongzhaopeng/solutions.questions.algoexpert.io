# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_InterweavingStrings_Hard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        one = "algoexpert"
        two = "your-dream-job"
        three = "your-algodream-expertjob"
        self.assertEqual(program.interweavingStrings(one, two, three), True)
