# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Algorithmic Beauty Bless You - O(d) time | O(1) space
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    searching_3, searching_1 = nodeOne, nodeThree
    found_3_from_1, found_1_from_3 = False, False
    while True:
        found_2 = searching_3 is nodeTwo or searching_1 is nodeTwo
        if found_2:
            break
        found_3_from_1 = searching_3 is nodeThree
        if found_3_from_1:
            break
        found_1_from_3 = searching_1 is nodeOne
        if found_1_from_3:
            break
        if not searching_3 and not searching_1:
            break
        if searching_3:
            searching_3 = searching_3.left if searching_3.value > nodeTwo.value else searching_3.right
        if searching_1:
            searching_1 = searching_1.left if searching_1.value > nodeTwo.value else searching_1.right
    if not found_2 or found_3_from_1 or found_1_from_3:
        return False
    return is_descendent(nodeTwo, nodeThree if searching_3 is nodeTwo else nodeOne)


def is_descendent(node, descend_x):
    while node and node is not descend_x:
        node = node.left if descend_x.value < node.value else node.right
    return bool(node)
