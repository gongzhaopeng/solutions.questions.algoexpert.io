# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Algorithmic Beauty Bless You - O(n) time | O(h) space
def mergeBinaryTrees(tree1, tree2):
    current, stack = [tree1, tree2], []
    while True:
        if current:
            root1, root2 = current
            root1.value += root2.value
            stack.append(current)
            current = None
            if not root1.left:
                root1.left = root2.left
            elif root2.left:
                current = [root1.left, root2.left]
        elif stack:
            root1, root2 = stack.pop()
            current = None
            if not root1.right:
                root1.right = root2.right
            elif root2.right:
                current = [root1.right, root2.right]
        else:
            break
    return tree1
