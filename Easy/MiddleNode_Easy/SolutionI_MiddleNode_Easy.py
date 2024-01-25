# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Algorithmic Beauty Bless You - O(n) time | O(1) space
def middleNode(linkedList):
    fast_node, slow_node = linkedList, linkedList
    while fast_node and fast_node.next:
        slow_node = slow_node.next
        fast_node = fast_node.next.next
    return slow_node
