import SolutionI_EvaluateExpressionTree_Easy as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree = program.BinaryTree(-1)
        tree.left = program.BinaryTree(2)
        tree.right = program.BinaryTree(-2)
        tree.right.left = program.BinaryTree(5)
        tree.right.right = program.BinaryTree(1)
        expected = 6
        actual = program.evaluateExpressionTree(tree)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        tree = program.BinaryTree(-3)
        tree.left = program.BinaryTree(2)
        tree.right = program.BinaryTree(3)
        expected = 0
        actual = program.evaluateExpressionTree(tree)
        self.assertEqual(actual, expected)
