# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Algorithmic Beauty Bless You - O(n) time | O(h) space
def heightBalancedBinaryTree(tree):
    current, stack = [tree, 0, 0, 0], []
    while True:
        if current[0]:
            stack.append(current)
            current = [current[0].left, 0, 0, 0]
        elif stack:
            stack[-1][1] += 1
            if stack[-1][1] > 1:
                *_, h_left, h_right = stack.pop()
                if abs(h_left - h_right) > 1:
                    return False
                height = max(h_left, h_right) + 1
                if stack:
                    if stack[-1][1] == 0:
                        stack[-1][2] = height
                    else:
                        stack[-1][3] = height
            else:
                current = [stack[-1][0].right, 0, 0, 0]
        else:
            break
    return True
