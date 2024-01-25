# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_LongestStringChain_VeryHard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        strings = ["abde", "abc", "abd", "abcde", "ade", "ae", "1abde", "abcdef"]
        expected = ["abcdef", "abcde", "abde", "ade", "ae"]
        self.assertEqual(program.longestStringChain(strings), expected)
