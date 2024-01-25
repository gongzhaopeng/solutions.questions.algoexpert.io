# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_ShortenPath_Hard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        expected = "/foo/bar/baz"
        output = program.shortenPath("/foo/../test/../test/../foo//bar/./baz")
        self.assertEqual(output, expected)

    def test_case_2(self):
        expected = "../../foo/bar/baz"
        output = program.shortenPath("../../foo/bar/baz")
        self.assertEqual(output, expected)

    def test_case_3(self):
        expected = "/"
        output = program.shortenPath(
            "/../../../this////one/./../../is/../../going/../../to/be/./././../../../just/a/forward/slash"
            "/../../../../../..")
        self.assertEqual(output, expected)
