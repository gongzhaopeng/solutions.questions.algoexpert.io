# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Algorithmic Beauty Bless You - O(n) time | O(1) space
def removeDuplicatesFromLinkedList(linkedList):
    pre = linkedList
    while pre:
        cur = pre.next
        if cur and pre.value == cur.value:
            pre.next = cur.next
        else:
            pre = cur
    return linkedList
