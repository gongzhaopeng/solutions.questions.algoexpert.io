# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Algorithmic Beauty Bless You - O(h+k) time | O(h) space
def findKthLargestValueInBst(tree, k):
    current, stack = tree, []
    while True:
        if current:
            stack.append(current)
            current = current.right
        elif stack:
            popped, k = stack.pop(), k - 1
            if k == 0:
                return popped.value
            current = popped.left
        else:
            break
