# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, node):
        self.node = node
        self.min_value = node.value
        self.max_value = node.value
        self.l_checked = False
        self.is_bst = True
        self.count = 1
        self.sum_to_merge = node.value


# Algorithmic Beauty Bless You - O(n) time | O(h) space
def sumBsts(tree):
    final_sum, stack = 0, []
    current = TreeInfo(tree)
    while True:
        if current and not current.l_checked:
            stack.append(current)
            current = TreeInfo(current.node.left) if current.node.left else None
        elif stack:
            parent = stack[-1]
            if not parent.l_checked:
                parent.l_checked = True
                if current:
                    if not current.is_bst or current.max_value >= parent.node.value:
                        parent.is_bst = False
                    if parent.is_bst:
                        parent.min_value = current.min_value
                        parent.count += current.count
                        parent.sum_to_merge += current.sum_to_merge
                current = TreeInfo(parent.node.right) if parent.node.right else None
            else:
                stack.pop()
                if current:
                    if not current.is_bst or current.min_value < parent.node.value:
                        parent.is_bst = False
                    if parent.is_bst:
                        parent.max_value = current.max_value
                        parent.count += current.count
                        parent.sum_to_merge += current.sum_to_merge
                if parent.is_bst and parent.count >= 3:
                    final_sum += parent.sum_to_merge
                    parent.sum_to_merge = 0
                current = parent
        else:
            break
    return final_sum
