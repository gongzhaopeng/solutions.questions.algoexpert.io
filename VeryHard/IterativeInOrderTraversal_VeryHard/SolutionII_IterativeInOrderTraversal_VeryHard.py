# Think that all the leaf nodes are None node.
# O(n) time | O(logn) space@average - Algorithmic Beauty Bless You
def iterativeInOrderTraversal(tree, callback):
    stack = []
    new_node = tree
    while True:
        if new_node:
            stack.append(new_node)
            new_node = new_node.left
        elif stack:
            parent_node = stack.pop()
            callback(parent_node)
            new_node = parent_node.right
        else:
            break
