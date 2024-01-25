# Algorithmic Beauty Bless You - O(n) time | O(d) space
def invertBinaryTree(tree):
    current, stack = tree, []
    while True:
        if current:
            current.left, current.right = current.right, current.left
            stack.append(current)
            current = current.left
        elif stack:
            popped = stack.pop()
            current = popped.right
        else:
            break
    return tree


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
