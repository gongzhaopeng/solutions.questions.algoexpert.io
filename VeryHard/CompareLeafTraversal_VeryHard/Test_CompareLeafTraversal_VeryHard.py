import SolutionII_CompareLeafTraversal_VeryHard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree1 = program.BinaryTree(1)
        tree1.left = program.BinaryTree(2)
        tree1.right = program.BinaryTree(3)
        tree1.left.left = program.BinaryTree(4)
        tree1.left.right = program.BinaryTree(5)
        tree1.right.right = program.BinaryTree(6)
        tree1.left.right.left = program.BinaryTree(7)
        tree1.left.right.right = program.BinaryTree(8)

        tree2 = program.BinaryTree(1)
        tree2.left = program.BinaryTree(2)
        tree2.right = program.BinaryTree(3)
        tree2.left.left = program.BinaryTree(4)
        tree2.left.right = program.BinaryTree(7)
        tree2.right.right = program.BinaryTree(5)
        tree2.right.right.left = program.BinaryTree(8)
        tree2.right.right.right = program.BinaryTree(6)

        expected = True
        actual = program.compareLeafTraversal(tree1, tree2)

        self.assertEqual(actual, expected)

    def test_case_2(self):
        tree1 = program.BinaryTree(1)
        tree1.left = program.BinaryTree(2)
        tree1.left.left = program.BinaryTree(3)
        tree1.left.left.right = program.BinaryTree(4)
        tree1.left.left.right.left = program.BinaryTree(5)

        tree2 = program.BinaryTree(1)
        tree2.right = program.BinaryTree(2)
        tree2.right.right = program.BinaryTree(3)
        tree2.right.right.left = program.BinaryTree(4)
        tree2.right.right.left.right = program.BinaryTree(5)

        expected = True
        actual = program.compareLeafTraversal(tree1, tree2)

        self.assertEqual(actual, expected)

    def test_case_3(self):
        tree1 = program.BinaryTree(1)
        tree1.left = program.BinaryTree(2)
        tree1.right = program.BinaryTree(3)
        tree1.left.left = program.BinaryTree(4)
        tree1.left.right = program.BinaryTree(5)
        tree1.right.right = program.BinaryTree(6)
        tree1.left.right.left = program.BinaryTree(7)
        tree1.left.right.right = program.BinaryTree(8)

        tree2 = program.BinaryTree(1)
        tree2.left = program.BinaryTree(2)
        tree2.right = program.BinaryTree(3)
        tree2.left.left = program.BinaryTree(4)
        tree2.left.right = program.BinaryTree(7)
        tree2.right.right = program.BinaryTree(5)
        tree2.right.right.left = program.BinaryTree(8)
        tree2.right.right.right = program.BinaryTree(6)
        tree2.right.right.left.left = program.BinaryTree(9)

        expected = False
        actual = program.compareLeafTraversal(tree1, tree2)

        self.assertEqual(actual, expected)
