from collections import deque


# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Algorithmic Beauty Bless You - O(n) time | O(n) space
def rightSiblingTree(root):
    queue = deque([(root, None)])
    while queue:
        current, sibling = queue.popleft()
        if current.left:
            queue.append((current.left, current.right))
        if current.right:
            if sibling:
                queue.append((current.right, sibling.left))
            else:
                queue.append((current.right, None))
        current.right = sibling
    return root
