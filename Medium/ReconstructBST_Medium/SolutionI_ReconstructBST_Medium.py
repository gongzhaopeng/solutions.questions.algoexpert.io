# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Algorithmic Beauty Bless You - O(n) time | O(n) space
def reconstructBst(preOrderTraversalValues):
    tree = BST(preOrderTraversalValues[0])
    i, current, stack = 0, (tree, float('inf')), []
    while i < len(preOrderTraversalValues) - 1:
        if current:
            stack.append(current)
            root, _ = current
            if preOrderTraversalValues[i + 1] < root.value:
                root.left = BST(preOrderTraversalValues[i + 1])
                current = (root.left, root.value)
                i += 1
            else:
                current = None
        elif stack:
            root, v_max = stack.pop()
            if preOrderTraversalValues[i + 1] < v_max:
                root.right = BST(preOrderTraversalValues[i + 1])
                current = (root.right, v_max)
                i += 1
            else:
                current = None
    return tree
