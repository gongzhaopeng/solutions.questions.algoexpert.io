# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Algorithmic Beauty Bless You - O(n) time | O(d) space
def rightSiblingTree(root):
    stack, l_siblings, l_sibling_cnt = [], [], 0
    current, depth = root, 0
    while True:
        if current:
            stack.append((current, depth))
            if depth < l_sibling_cnt:
                l_siblings[depth].right = current
            if depth < len(l_siblings):
                l_siblings[depth] = current
            else:
                l_siblings.append(current)
            current = current.left
        elif stack:
            l_sibling_cnt = depth
            popped, depth = stack.pop()
            current = popped.right
            popped.right = None
        else:
            break
        depth += 1
    return root
