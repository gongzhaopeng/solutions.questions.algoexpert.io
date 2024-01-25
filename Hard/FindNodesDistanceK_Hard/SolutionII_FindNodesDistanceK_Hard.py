# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Algorithmic Beauty Bless You - O(n) time | O(n) space
def findNodesDistanceK(tree, target, k):
    matches = []
    search_k_dis_nodes(tree, target, k, matches)
    return matches


def search_k_dis_nodes(root, target, k, matches):
    if not root:
        return -1
    if root.value == target:
        search_by_depth(root, 0, k, matches)
        return 1
    l_dis = search_k_dis_nodes(root.left, target, k, matches)
    if l_dis == k:
        matches.append(root.value)
    elif 0 < l_dis < k:
        search_by_depth(root.right, 0, k - l_dis - 1, matches)
    elif l_dis < 0:
        r_dis = search_k_dis_nodes(root.right, target, k, matches)
        if r_dis == k:
            matches.append(root.value)
        elif 0 < r_dis < k:
            search_by_depth(root.left, 0, k - r_dis - 1, matches)
        elif r_dis < 0:
            return -1
        return r_dis + 1
    return l_dis + 1


def search_by_depth(root, depth, specified_depth, matches):
    if not root:
        return
    if depth == specified_depth:
        matches.append(root.value)
    else:
        search_by_depth(root.left, depth + 1, specified_depth, matches)
        search_by_depth(root.right, depth + 1, specified_depth, matches)
