# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Algorithmic Beauty Bless You - O(n) time | O(1) space
def removeKthNodeFromEnd(head, k):
    length, current = 0, head
    while current:
        length, current = length + 1, current.next
    pre, current = None, head
    for _ in range(length - k):
        pre, current = current, current.next
    if current.next:
        current.value, current.next = current.next.value, current.next.next
    else:
        pre.next = current.next
