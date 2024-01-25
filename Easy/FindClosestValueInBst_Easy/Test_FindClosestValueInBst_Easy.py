import unittest
from SolutionI_FindClosestValueInBst_Easy import findClosestValueInBst, BST


class TestFindClosestValueInBst(unittest.TestCase):
    def test_case1(self):
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)
        expected = 13

        self.assertEqual(expected, findClosestValueInBst(root, 12))


if __name__ == '__main__':
    unittest.main()
