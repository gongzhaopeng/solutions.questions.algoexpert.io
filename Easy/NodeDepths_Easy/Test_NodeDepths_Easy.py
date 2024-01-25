import unittest
import SolutionI_NodeDepths_Easy as program


class TestNodeDepths(unittest.TestCase):
    def test_case1(self):
        root = program.BinaryTree(1)
        root.left = program.BinaryTree(2)
        root.left.left = program.BinaryTree(4)
        root.left.left.left = program.BinaryTree(8)
        root.left.left.right = program.BinaryTree(9)
        root.left.right = program.BinaryTree(5)
        root.right = program.BinaryTree(3)
        root.right.left = program.BinaryTree(6)
        root.right.right = program.BinaryTree(7)
        expected = 16
        self.assertEqual(expected, program.nodeDepths(root))


if __name__ == '__main__':
    unittest.main()
