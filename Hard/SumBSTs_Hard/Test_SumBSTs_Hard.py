# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_SumBSTs_Hard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = program.BinaryTree(8)
        root.left = program.BinaryTree(2)
        root.left.left = program.BinaryTree(1)
        root.left.right = program.BinaryTree(10)
        root.right = program.BinaryTree(9)
        root.right.right = program.BinaryTree(5)
        expected = 13
        actual = program.sumBsts(root)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        root = program.BinaryTree(8)
        root.left = program.BinaryTree(2)
        root.left.left = program.BinaryTree(1)
        root.left.right = program.BinaryTree(10)
        root.right = program.BinaryTree(9)
        expected = 13
        actual = program.sumBsts(root)
        self.assertEqual(actual, expected)
