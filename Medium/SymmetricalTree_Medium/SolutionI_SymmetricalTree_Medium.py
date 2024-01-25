# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Algorithmic Beauty Bless You - O(n) time | O(h) space
def symmetricalTree(tree):
    stack = [(tree.left, tree.right)]
    while stack:
        root1, root2 = stack.pop()
        if not root1 and not root2:
            continue
        if not root1 or not root2 or root1.value != root2.value:
            return False
        stack.append((root1.right, root2.left))
        stack.append((root1.left, root2.right))
    return True
