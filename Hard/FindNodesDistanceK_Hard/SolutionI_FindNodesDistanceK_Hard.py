# This is an input class. Do not edit.
import operator


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Algorithmic Beauty Bless You - O(n) time | O(n) space
def findNodesDistanceK(tree, target, k):
    matches = []
    target_path = get_target_path(tree, target)
    path_len = len(target_path)
    if path_len > k:
        matches.append(target_path[-(k + 1)])
    first_search_pos = max(path_len - k, 0)
    for i in range(first_search_pos, path_len - 1):
        remain_dis = k - (path_len - i)
        if target_path[i].left is target_path[i + 1]:
            search_root = target_path[i].right
        else:
            search_root = target_path[i].left
        search_nodes_of_depth(search_root, remain_dis, matches)
    search_nodes_of_depth(target_path[-1].left, k - 1, matches)
    search_nodes_of_depth(target_path[-1].right, k - 1, matches)
    return list(map(operator.attrgetter('value'), matches))


def search_nodes_of_depth(root, specified_depth, matches):
    if root is None:
        return
    stack, current = [], [root, 0]
    while True:
        if current[0]:
            node, depth = current
            if depth == specified_depth:
                matches.append(node)
                current = [None, None]
            else:
                stack.append(current)
                current = [node.left, depth + 1]
        elif stack:
            node, depth = stack.pop()
            current = [node.right, depth + 1]
        else:
            break


def get_target_path(tree, target):
    target_path, path_len, stack, current = [], 0, [], [tree, 0]
    while True:
        if current[0]:
            node, depth = current
            if depth < len(target_path):
                target_path[depth] = node
            else:
                target_path.append(node)
            if node.value == target:
                path_len = depth + 1
                break
            stack.append(current)
            current = [node.left, depth + 1]
        elif stack:
            node, depth = stack.pop()
            current = [node.right, depth + 1]
        else:
            break
    target_path[path_len:] = []
    return target_path
