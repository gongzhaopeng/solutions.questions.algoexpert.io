# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_ValidIpAddresses_Medium as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = "1921680"
        expected = [
            "1.9.216.80",
            "1.92.16.80",
            "1.92.168.0",
            "19.2.16.80",
            "19.2.168.0",
            "19.21.6.80",
            "19.21.68.0",
            "19.216.8.0",
            "192.1.6.80",
            "192.1.68.0",
            "192.16.8.0",
        ]
        actual = program.validIPAddresses(input)
        self.assertCountEqual(actual, expected)
