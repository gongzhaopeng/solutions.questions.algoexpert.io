# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_ZipLinkedList_VeryHard as program
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
        head = LinkedList(1).addMany([2, 3, 4, 5, 6])
        expected = [1, 6, 2, 5, 3, 4]
        actual = program.zipLinkedList(head).getNodesInArray()
        self.assertEqual(actual, expected)

    def test_case_2(self):
        head = LinkedList(1).addMany([2, 3, 4, 5, 6, 7])
        expected = [1, 7, 2, 6, 3, 5, 4]
        actual = program.zipLinkedList(head).getNodesInArray()
        self.assertEqual(actual, expected)
