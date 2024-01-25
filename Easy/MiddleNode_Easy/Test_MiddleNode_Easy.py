# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_MiddleNode_Easy as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        linkedList = program.LinkedList(0)
        linkedList.next = program.LinkedList(1)
        expected = program.LinkedList(2)
        linkedList.next.next = expected
        expected.next = program.LinkedList(3)
        actual = program.middleNode(linkedList)
        self.assertEqual(actual, expected)
