import unittest
from SolutionI_BranchSums_Easy import branchSums, BinaryTree as _BTree


class TestBranchSums(unittest.TestCase):
    def test_case1(self):
        tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])
        expected = [15, 16, 18, 10, 11]
        self.assertEqual(expected, branchSums(tree))


class BinaryTree(_BTree):
    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self


if __name__ == '__main__':
    unittest.main()
