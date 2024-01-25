# Algorithmic Beauty Bless You - O(n) time | O(d) space
def allKindsOfNodeDepths(root):
    sum_all = 0
    stack = []
    current, depth, depth_sum = root, 0, 0
    while True:
        if current:
            depth_sum += depth
            sum_all += depth_sum
            stack.append((current, depth, depth_sum))
            current, depth = current.left, depth + 1
        elif stack:
            popped, depth, depth_sum = stack.pop()
            current, depth = popped.right, depth + 1
        else:
            break
    return sum_all


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
