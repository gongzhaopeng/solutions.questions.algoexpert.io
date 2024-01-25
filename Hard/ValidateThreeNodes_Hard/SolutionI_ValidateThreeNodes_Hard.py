# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Algorithmic Beauty Bless You - O(d) time | O(1) space
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    if is_descendent(nodeTwo, nodeOne):
        return is_descendent(nodeThree, nodeTwo)
    return is_descendent(nodeTwo, nodeThree) and is_descendent(nodeOne, nodeTwo)


def is_descendent(node, descend_x):
    while node and node is not descend_x:
        node = node.left if descend_x.value < node.value else node.right
    return bool(node)
