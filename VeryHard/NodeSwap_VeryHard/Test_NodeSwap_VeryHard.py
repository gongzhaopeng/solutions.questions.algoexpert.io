# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_NodeSwap_VeryHard as program
import unittest


class LinkedList(program.LinkedList):
    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        linkedList = LinkedList(0).addMany([1, 2, 3, 4, 5])
        expectedNodes = [1, 0, 3, 2, 5, 4]
        output = program.nodeSwap(linkedList)
        self.assertEqual(output.getNodesInArray(), expectedNodes)
