# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionII_ValidateThreeNodes_Hard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = program.BST(5)
        root.left = program.BST(2)
        root.right = program.BST(7)
        root.left.left = program.BST(1)
        root.left.right = program.BST(4)
        root.right.left = program.BST(6)
        root.right.right = program.BST(8)
        root.left.left.left = program.BST(0)
        root.left.right.left = program.BST(3)

        nodeOne = root
        nodeTwo = root.left
        nodeThree = root.left.right.left
        expected = True
        actual = program.validateThreeNodes(nodeOne, nodeTwo, nodeThree)
        self.assertEqual(actual, expected)
