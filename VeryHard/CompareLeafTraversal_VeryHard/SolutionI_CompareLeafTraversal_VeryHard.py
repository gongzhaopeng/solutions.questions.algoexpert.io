# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Algorithmic Beauty Bless You - O(n1+n2) time | O(h1+h2) space
def compareLeafTraversal(tree1, tree2):
    traverse_1, traverse_2 = traverse_leafs(tree1), traverse_leafs(tree2)
    while True:
        next_leaf_1, next_leaf_2 = next(traverse_1), next(traverse_2)
        if not next_leaf_1:
            return not next_leaf_2
        elif not next_leaf_2 or next_leaf_1.value != next_leaf_2.value:
            return False


def traverse_leafs(tree):
    stack, current = [], tree
    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            popped = stack.pop()
            if not popped.right:
                if not popped.left:
                    yield popped
                current = None
            else:
                current = popped.right
        else:
            break
    yield None
