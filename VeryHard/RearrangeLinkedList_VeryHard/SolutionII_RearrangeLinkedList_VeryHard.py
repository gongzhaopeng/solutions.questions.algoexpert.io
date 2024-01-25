# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Algorithmic Beauty Bless You - O(n) time | O(1) space
def rearrangeLinkedList(head, k):
    less_head = less_tail = LinkedList(None)
    equal_head = equal_tail = LinkedList(None)
    greater_head = greater_tail = LinkedList(None)
    current = head
    while current:
        if current.value < k:
            less_tail.next = less_tail = current
        elif current.value > k:
            greater_tail.next = greater_tail = current
        else:
            equal_tail.next = equal_tail = current
        current = current.next
    equal_tail.next, greater_tail.next = greater_head.next, None
    less_tail.next = equal_head.next
    return less_head.next
