# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, root):
        self.is_bst = True
        self.min_value = root.value
        self.max_value = root.value
        self.count = 1
        self.sum_to_merge = root.value
        self.final_sum = 0


# Algorithmic Beauty Bless You - O(n) time | O(h) space
def sumBsts(tree):
    return get_tree_info(tree).final_sum


def get_tree_info(root):
    tree_info = TreeInfo(root)
    if root.left:
        left_tree_info = get_tree_info(root.left)
        if not left_tree_info.is_bst or left_tree_info.max_value >= root.value:
            tree_info.is_bst = False
        if tree_info.is_bst:
            tree_info.min_value = left_tree_info.min_value
            tree_info.count += left_tree_info.count
            tree_info.sum_to_merge += left_tree_info.sum_to_merge
        tree_info.final_sum += left_tree_info.final_sum
    if root.right:
        right_tree_info = get_tree_info(root.right)
        if not right_tree_info.is_bst or right_tree_info.min_value < root.value:
            tree_info.is_bst = False
        if tree_info.is_bst:
            tree_info.max_value = right_tree_info.max_value
            tree_info.count += right_tree_info.count
            tree_info.sum_to_merge += right_tree_info.sum_to_merge
        tree_info.final_sum += right_tree_info.final_sum
    if tree_info.is_bst and tree_info.count >= 3:
        tree_info.final_sum += tree_info.sum_to_merge
        tree_info.sum_to_merge = 0
    return tree_info
