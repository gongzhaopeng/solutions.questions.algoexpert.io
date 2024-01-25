# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # Algorithmic Beauty Bless You - O(n) time | O(n) space
    def depthFirstSearch(self, array):
        stack = []
        current, pos = self, 0
        while True:
            if current:
                array.append(current.name)
                stack.append([current, 0])
                current = current.children[0] if current.children else None
            elif stack:
                popped, pos = stack[-1]
                pos += 1
                if pos < len(popped.children):
                    stack[-1][1] = pos
                    current = popped.children[pos]
                else:
                    stack.pop()
                    current = None
            else:
                break
        return array
