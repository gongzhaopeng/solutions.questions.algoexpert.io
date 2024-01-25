# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Algorithmic Beauty Bless You - O(n) time | O(1) space
def removeDuplicatesFromLinkedList(linkedList):
    cur = linkedList
    while cur.next:
        if cur.value == cur.next.value:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return linkedList
