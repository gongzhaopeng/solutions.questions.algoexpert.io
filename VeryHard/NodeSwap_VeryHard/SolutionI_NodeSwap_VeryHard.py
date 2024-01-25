# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Algorithmic Beauty Bless You - O(n) time | O(1) space
def nodeSwap(head):
    pre = LinkedList(None)
    pre.next = a = head
    head = pre
    while a and a.next:
        b = a.next
        pre.next, b.next, pre, a = b, a, a, b.next
    pre.next = a
    return head.next
