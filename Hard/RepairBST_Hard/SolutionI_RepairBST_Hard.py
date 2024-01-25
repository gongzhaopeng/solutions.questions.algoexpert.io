# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Algorithmic Beauty Bless You - O(n) time | O(h) space
def repairBst(tree):
    stack, current, pre, spot_1 = [], tree, BST(float('-inf')), None
    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            popped = stack.pop()
            if not spot_1:
                if popped.value < pre.value:
                    spot_1 = pre
            elif popped.value > spot_1.value:
                break
            pre, current = popped, popped.right
        else:
            break
    spot_1.value, pre.value = pre.value, spot_1.value
    return tree
