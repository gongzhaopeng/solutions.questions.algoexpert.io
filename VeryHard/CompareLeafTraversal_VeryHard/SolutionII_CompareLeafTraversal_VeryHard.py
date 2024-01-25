# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Algorithmic Beauty Bless You - O(n1+n2) time | O(h1+h2) space
def compareLeafTraversal(tree1, tree2):
    cur_1, cur_2 = link_leafs(tree1), link_leafs(tree2)
    while True:
        if cur_1:
            if cur_2:
                if cur_1.value != cur_2.value:
                    return False
            else:
                return False
        else:
            return not cur_2
        cur_1, cur_2 = cur_1.right, cur_2.right


def link_leafs(tree):
    head, pre, stack = None, None, [tree]
    while stack:
        current = stack.pop()
        if current.right:
            stack.append(current.right)
            if current.left:
                stack.append(current.left)
        elif current.left:
            stack.append(current.left)
        else:
            if not head:
                head = current
            if pre:
                pre.right = current
            pre = current
    return head
