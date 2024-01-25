from collections import deque


# Algorithmic Beauty Bless You - O(n) time | O(n) space
def allKindsOfNodeDepths(root):
    sum_all = 0
    depth_sum = 0
    queue = deque([(root, 0, 0)])
    while queue:
        popped, depth, depth_sum = queue.popleft()
        depth_sum += depth
        sum_all += depth_sum
        if popped.left:
            queue.append((popped.left, depth + 1, depth_sum))
        if popped.right:
            queue.append((popped.right, depth + 1, depth_sum))
    return sum_all


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
