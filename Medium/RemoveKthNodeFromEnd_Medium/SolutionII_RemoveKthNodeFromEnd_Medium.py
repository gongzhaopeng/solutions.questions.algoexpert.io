# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Algorithmic Beauty Bless You - O(n) time | O(1) space
def removeKthNodeFromEnd(head, k):
    current = head
    for _ in range(k):
        current = current.next
    if current is None:
        head.value, head.next = head.next.value, head.next.next
        return
    while current.next:
        current, head = current.next, head.next
    head.next = head.next.next
