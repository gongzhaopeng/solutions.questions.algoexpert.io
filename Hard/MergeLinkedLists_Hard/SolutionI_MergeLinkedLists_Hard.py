# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Algorithmic Beauty Bless You - O(n+m) time | O(1) space
def mergeLinkedLists(headOne, headTwo):
    if headOne.value > headTwo.value:
        headOne, headTwo = headTwo, headOne
    sorted_head, sorted_tail, headOne = headOne, headOne, headOne.next
    while True:
        if headOne is None:
            sorted_tail.next = headTwo
            break
        if headOne.value > headTwo.value:
            headOne, headTwo = headTwo, headOne
        sorted_tail.next, sorted_tail, headOne = headOne, headOne, headOne.next
    return sorted_head
