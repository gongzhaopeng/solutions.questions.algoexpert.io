def findClosestValueInBst(tree, target):
    closest_top_left_ancient = BST(float('-inf'))
    closest_top_right_ancient = BST(float('inf'))
    cur_node = tree
    while cur_node:
        if target < cur_node.value:
            closest_top_right_ancient = cur_node
            cur_node = cur_node.left
        elif target > cur_node.value:
            closest_top_left_ancient = cur_node
            cur_node = cur_node.right
        else:
            return cur_node.value
    if target - closest_top_left_ancient.value < closest_top_right_ancient.value - target:
        return closest_top_left_ancient.value
    else:
        return closest_top_right_ancient.value


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
