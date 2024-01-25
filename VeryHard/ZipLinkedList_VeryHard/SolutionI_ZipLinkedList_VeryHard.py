# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Algorithmic Beauty Bless You - O(n) time | O(1) space
def zipLinkedList(linkedList):
    single = double = linkedList
    while double and double.next:
        single, double = single.next, double.next.next
    if double:
        single = single.next
    head, rev = linkedList, None
    while single:
        single.next, rev, single = rev, single, single.next
    while rev:
        linkedList.next, linkedList, rev.next, rev = rev, linkedList.next, linkedList.next, rev.next
    if linkedList:
        linkedList.next = None
    return head
