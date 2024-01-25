# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Algorithmic Beauty Bless You - O(1) time | O(1) space
    def setHead(self, node):
        if self.head is None:
            self.head = self.tail = node
            return
        self.insertBefore(self.head, node)

    # Algorithmic Beauty Bless You - O(1) time | O(1) space
    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    # Algorithmic Beauty Bless You - O(1) time | O(1) space
    def insertBefore(self, node, nodeToInsert):
        self.remove(nodeToInsert)
        if node.prev:
            node.prev.next = nodeToInsert
        nodeToInsert.prev, nodeToInsert.next, node.prev = node.prev, node, nodeToInsert
        if node is self.head:
            self.head = nodeToInsert

    # Algorithmic Beauty Bless You - O(1) time | O(1) space
    def insertAfter(self, node, nodeToInsert):
        self.remove(nodeToInsert)
        if node.next:
            node.next.prev = nodeToInsert
        nodeToInsert.prev, nodeToInsert.next, node.next = node, node.next, nodeToInsert
        if node is self.tail:
            self.tail = nodeToInsert

    # Algorithmic Beauty Bless You - O(p) time | O(1) space
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        next_node = self.head
        for _ in range(position - 1):
            next_node = next_node.next
        if not next_node:
            self.setTail(nodeToInsert)
            return
        if next_node is nodeToInsert:
            return
        self.insertBefore(next_node, nodeToInsert)

    # Algorithmic Beauty Bless You - O(n) time | O(1) space
    def removeNodesWithValue(self, value):
        cur_node = self.head
        while True:
            node_to_remove = next_node_with_value(cur_node, value)
            if node_to_remove is None:
                break
            cur_node = node_to_remove.next
            self.remove(node_to_remove)

    # Algorithmic Beauty Bless You - O(1) time | O(1) space
    def remove(self, node):
        if node is self.head:
            self.head = node.next
        if node is self.tail:
            self.tail = node.prev
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.prev, node.next = None, None

    # Algorithmic Beauty Bless You - O(n) time | O(1) space
    def containsNodeWithValue(self, value):
        return next_node_with_value(self.head, value) is not None


def next_node_with_value(start_node, value):
    while start_node and start_node.value != value:
        start_node = start_node.next
    return start_node
