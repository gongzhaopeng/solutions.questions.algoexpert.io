# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_GroupAnagrams_Medium as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
        expected = [["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]
        output = list(map(lambda x: sorted(x), program.groupAnagrams(words)))

        self.compare(expected, output)

    def compare(self, expected, output):
        if len(expected) == 0:
            self.assertEqual(output, expected)
            return
        self.assertEqual(len(expected), len(output))
        for group in expected:
            self.assertTrue(sorted(group) in output)
