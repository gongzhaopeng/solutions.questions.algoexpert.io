from collections import deque


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Algorithmic Beauty Bless You - O(n) time | O(n) space
def findNodesDistanceK(tree, target, k):
    node_to_parent = {}
    map_node_to_parent(tree, node_to_parent)
    target_node = get_target_node(tree, target, node_to_parent)
    return bfs_for_k_dis(target_node, k, node_to_parent)


def bfs_for_k_dis(origin_node, k, node_to_parent):
    queue = deque([(origin_node, 0)])
    visited = {origin_node.value}
    while queue:
        current, dis = queue.popleft()
        if dis == k:
            return [elem[0].value for elem in queue] + [current.value]
        for neighbor in [current.left, current.right, node_to_parent.get(current.value, None)]:
            if neighbor and neighbor.value not in visited:
                queue.append((neighbor, dis + 1))
                visited.add(neighbor.value)
    return []


def get_target_node(tree, target, node_to_parent):
    if tree.value == target:
        return tree
    parent = node_to_parent[target]
    return parent.left if parent.left and parent.left.value == target else parent.right


def map_node_to_parent(tree, node_to_parent):
    if tree.left:
        node_to_parent[tree.left.value] = tree
        map_node_to_parent(tree.left, node_to_parent)
    if tree.right:
        node_to_parent[tree.right.value] = tree
        map_node_to_parent(tree.right, node_to_parent)
