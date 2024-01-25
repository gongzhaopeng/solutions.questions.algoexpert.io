# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Algorithmic Beauty Bless You - O(n) time | O(logn) space
def flattenBinaryTree(root):
    stack = []
    left_most, pre, current = None, None, root
    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            popped = stack.pop()
            if not left_most:
                left_most = popped
            if pre:
                pre.right = popped
            popped.left = pre
            pre = popped
            current = popped.right
        else:
            break
    left_most.left = None
    pre.right = None
    return left_most
