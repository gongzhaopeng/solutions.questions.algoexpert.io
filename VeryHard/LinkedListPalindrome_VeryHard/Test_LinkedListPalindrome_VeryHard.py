# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_LinkedListPalindrome_VeryHard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        head = program.LinkedList(0)
        # head.next = program.LinkedList(1)
        # head.next.next = program.LinkedList(2)
        # head.next.next.next = program.LinkedList(2)
        # head.next.next.next.next = program.LinkedList(1)
        # head.next.next.next.next.next = program.LinkedList(0)
        expected = True
        actual = program.linkedListPalindrome(head)
        self.assertEqual(actual, expected)
