# Algorithmic Beauty Bless You - O(n) time | O(logn) space@average
def branchSums(root):
    sums = []
    right_children = []
    ancients_sum = 0
    while True:
        if root:
            ancients_sum += root.value
            if root.right:
                right_children.append((root.right, ancients_sum))
            elif not root.left:
                sums.append(ancients_sum)
            root = root.left
        elif right_children:
            root, ancients_sum = right_children.pop()
        else:
            break
    return sums


# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
