# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Algorithmic Beauty Bless You - O(n) time | O(h) space
def mergeBinaryTrees(tree1, tree2):
    stack = [(tree1, tree2)]
    while stack:
        root1, root2 = stack.pop()
        if not root2:
            continue
        root1.value += root2.value
        if not root1.right:
            root1.right = root2.right
        else:
            stack.append((root1.right, root2.right))
        if not root1.left:
            root1.left = root2.left
        else:
            stack.append((root1.left, root2.left))
    return tree1
