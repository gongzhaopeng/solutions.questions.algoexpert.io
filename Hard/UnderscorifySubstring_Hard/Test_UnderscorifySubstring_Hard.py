# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_UnderscorifySubstring_Hard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            program.underscorifySubstring(
                "testthis is a testtest to see if testestest it works", "test"
            ),
            "_test_this is a _testtest_ to see if _testestest_ it works",
        )
