# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Algorithmic Beauty Bless You - O(max(m,n)) time | O(max(m,n)) space
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    sum_head, exceed = LinkedList(None), 0
    summ = sum_head
    while linkedListOne or linkedListTwo or exceed:
        summ.next = LinkedList(
            exceed + (linkedListOne.value if linkedListOne else 0) + (linkedListTwo.value if linkedListTwo else 0))
        summ = summ.next
        summ.value, exceed = summ.value % 10, summ.value // 10
        linkedListOne = linkedListOne.next if linkedListOne else None
        linkedListTwo = linkedListTwo.next if linkedListTwo else None
    return sum_head.next
