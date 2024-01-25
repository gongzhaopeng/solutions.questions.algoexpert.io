# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Algorithmic Beauty Bless You - O(n) time | O(d) space
def evaluateExpressionTree(tree):
    stack = []
    current, left_result = tree, None
    sub_result = None
    while True:
        if current:
            if current.value > 0:
                sub_result = current.value
                current = None
            else:
                stack.append([current, left_result])
                current, left_result = current.left, None
        elif stack:
            current, left_result = stack[-1]
            if not left_result:
                stack[-1][1] = sub_result
                current, left_result = current.right, None
            else:
                stack.pop()
                if current.value == -1:
                    sub_result = left_result + sub_result
                elif current.value == -2:
                    sub_result = left_result - sub_result
                elif current.value == -3:
                    sub_result = int(left_result / sub_result)
                else:
                    sub_result = left_result * sub_result
                current = None
        else:
            break
    return sub_result
