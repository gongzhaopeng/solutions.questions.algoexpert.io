# Algorithmic Beauty Bless You - O(n) time | O(logn) space
def nodeDepths(root):
    depths = 0
    stack = []
    current = root
    depth = 0
    while True:
        if current:
            stack.append([current, depth])
            current = current.left
            depth += 1
        elif stack:
            popped, depth = stack.pop()
            depths += depth
            current = popped.right
            depth += 1
        else:
            break
    return depths


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
