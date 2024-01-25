# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_MultiStringSearch_Hard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            program.multiStringSearch(
                "this is a big string", ["this", "yo", "is", "a", "bigger", "string", "kappa"]
            ),
            [True, False, True, True, False, True, False],
        )
