# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionII_StringsMadeUpOfStrings_VeryHard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        strings = ["bar", "are", "foo", "ba", "b", "barely"]
        substrings = ["b", "a", "r", "ba", "ar", "bar"]
        expected = ["bar", "ba", "b"]
        actual = program.stringsMadeUpOfStrings(strings, substrings)
        self.assertCountEqual(actual, expected)

    def test_case_2(self):
        strings = ["foobarbaz", "bazbarfoo", "foobaz", "quxquux", "quuxqux"]
        substrings = ["foo", "ba", "bar", "baz", "qux", "qu"]
        expected = ["bazbarfoo", "foobarbaz", "foobaz"]
        actual = program.stringsMadeUpOfStrings(strings, substrings)
        self.assertCountEqual(actual, expected)
