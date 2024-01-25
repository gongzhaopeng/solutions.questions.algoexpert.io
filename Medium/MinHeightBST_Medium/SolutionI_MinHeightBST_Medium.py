# Algorithmic Beauty Bless You - O(n) time | O(n) space
def minHeightBst(array):
    tree = BST(None)
    current, stack = [tree, 0, len(array) - 1, None], []
    while True:
        if current:
            stack.append(current)
            root, p_left, p_right, _ = current
            current[-1] = p_mid = (p_left + p_right) // 2
            root.value = array[p_mid]
            if p_mid - 1 >= p_left:
                root.left = BST(None)
                current = [root.left, p_left, p_mid - 1, None]
            else:
                current = None
        elif stack:
            root, _, p_right, p_mid = stack.pop()
            if p_mid + 1 <= p_right:
                root.right = BST(None)
                current = [root.right, p_mid + 1, p_right, None]
            else:
                current = None
        else:
            break
    return tree


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
