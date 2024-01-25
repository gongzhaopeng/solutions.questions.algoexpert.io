# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Algorithmic Beauty Bless You - O(n) time | O(1) space
def reverseLinkedList(head):
    pre, cur = None, head
    while cur:
        ne = cur.next
        cur.next = pre
        pre, cur = cur, ne
    return pre
