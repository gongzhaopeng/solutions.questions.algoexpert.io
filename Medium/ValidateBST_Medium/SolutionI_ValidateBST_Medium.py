# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Algorithmic Beauty Bless You - O(n) time | O(d) space
def validateBst(tree):
    pre, current, stack = BST(float('-inf')), tree, []
    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            popped = stack.pop()
            if popped.left:
                if pre.value >= popped.value:
                    return False
            elif pre.value > popped.value:
                return False
            pre, current = popped, popped.right
        else:
            break
    return True
