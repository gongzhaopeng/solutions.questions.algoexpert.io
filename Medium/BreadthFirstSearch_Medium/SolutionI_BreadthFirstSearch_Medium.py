# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # Algorithmic Beauty Bless You - O(n) time | O(1) space
    def breadthFirstSearch(self, array):
        p_cur = 0
        array.append(self)
        while p_cur < len(array):
            array.extend(array[p_cur].children)
            array[p_cur], p_cur = array[p_cur].name, p_cur + 1
        return array
