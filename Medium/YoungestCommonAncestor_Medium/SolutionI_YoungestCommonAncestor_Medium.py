# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


# Algorithmic Beauty Bless You - O(d) time | O(1) space
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    d1, d2 = get_depth(descendantOne), get_depth(descendantTwo)
    if d1 < d2:
        d1, d2, descendantOne, descendantTwo = d2, d1, descendantTwo, descendantOne
    for _ in range(d1 - d2):
        descendantOne = descendantOne.ancestor
    for _ in range(d2):
        if descendantOne is descendantTwo:
            break
        descendantOne, descendantTwo = descendantOne.ancestor, descendantTwo.ancestor
    return descendantOne


def get_depth(node):
    d = -1
    while node:
        d, node = d + 1, node.ancestor
    return d
