import unittest
from SolutionII_IterativeInOrderTraversal_VeryHard import iterativeInOrderTraversal


class TestWaterfallStreams(unittest.TestCase):
    def test_case1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2, parent=root)
        root.left.left = BinaryTree(4, parent=root.left)
        root.left.left.right = BinaryTree(9, parent=root.left.left)
        root.right = BinaryTree(3, parent=root)
        root.right.left = BinaryTree(6, parent=root.right)
        root.right.right = BinaryTree(7, parent=root.right)

        test_array = []
        iterativeInOrderTraversal(root, lambda x: testCallback(test_array, x))
        expected = [4, 9, 2, 1, 6, 3, 7]
        self.assertEqual(expected, test_array)


class BinaryTree:
    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent


def testCallback(testArray, tree):
    if tree is None:
        return
    testArray.append(tree.value)


if __name__ == '__main__':
    unittest.main()
