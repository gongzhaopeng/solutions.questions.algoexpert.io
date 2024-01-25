import unittest
from SolutionI_FlattenBinaryTree_VeryHard import flattenBinaryTree, BinaryTree as BTreeBase


class TestFlattenBinaryTree(unittest.TestCase):
    def test_case1(self):
        root = BinaryTree(1).insert([2, 3, 4, 5, 6])
        root.left.right.left = BinaryTree(7)
        root.left.right.right = BinaryTree(8)
        left_most_node = flattenBinaryTree(root)
        left_to_right_to_left = left_most_node.leftToRightToLeft()
        expected = [4, 2, 7, 5, 8, 1, 6, 3, 3, 6, 1, 8, 5, 7, 2, 4]
        self.assertEqual(expected, left_to_right_to_left)


class BinaryTree(BTreeBase):
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

    def leftToRightToLeft(self):
        nodes = []
        current = self
        while current.right is not None:
            nodes.append(current.value)
            current = current.right
        nodes.append(current.value)
        while current is not None:
            nodes.append(current.value)
            current = current.left
        return nodes


if __name__ == '__main__':
    unittest.main()
