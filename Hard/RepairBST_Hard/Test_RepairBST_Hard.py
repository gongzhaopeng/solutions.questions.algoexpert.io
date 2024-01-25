# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import SolutionI_RepairBST_Hard as program
import unittest


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree = BST(2)
        tree.left = BST(1)
        tree.right = BST(3)
        tree.left.left = BST(4)
        tree.right.right = BST(0)
        expected = [0, 1, 2, 3, 4]
        actual = inOrderTraverse(program.repairBst(tree), [])
        self.assertEqual(actual, expected)


def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array
