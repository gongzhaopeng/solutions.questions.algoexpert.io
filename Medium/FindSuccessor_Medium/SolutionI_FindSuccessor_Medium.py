# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


# Algorithmic Beauty Bless You - O(h) time | O(1) space
def findSuccessor(tree, node):
    if node.right:
        current = node.right
        while current.left:
            current = current.left
        return current
    while node.parent and node.parent.right is node:
        node = node.parent
    return node.parent
