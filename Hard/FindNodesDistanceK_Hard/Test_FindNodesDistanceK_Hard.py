# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionIII_FindNodesDistanceK_Hard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = program.BinaryTree(1)
        root.left = program.BinaryTree(2)
        root.right = program.BinaryTree(3)
        root.left.left = program.BinaryTree(4)
        root.left.right = program.BinaryTree(5)
        root.right.right = program.BinaryTree(6)
        root.right.right.left = program.BinaryTree(7)
        root.right.right.right = program.BinaryTree(8)
        target = 3
        k = 2
        expected = [2, 7, 8]
        actual = program.findNodesDistanceK(root, target, k)
        actual.sort()
        self.assertCountEqual(actual, expected)
