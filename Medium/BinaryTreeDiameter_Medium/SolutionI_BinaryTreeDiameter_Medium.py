# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Algorithmic Beauty Bless You - O(n) time | O(h) space
def binaryTreeDiameter(tree):
    current, stack = [tree, 0, 0, 0], []
    while True:
        if current[0]:
            stack.append(current)
            current = [current[0].left, 0, 0, 0]
        elif stack:
            stack[-1][1] += 1
            node, p_visiting, height, diameter = stack[-1]
            if p_visiting > 1:
                stack.pop()
                if stack:
                    stack[-1][3] = max(stack[-1][3], diameter, stack[-1][2] + height + 1)
                    stack[-1][2] = max(stack[-1][2], height + 1)
                else:
                    return diameter
            else:
                current = [node.right, 0, 0, 0]
