# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Algorithmic Beauty Bless You - O(m+n) time | O(1) space
def mergingLinkedLists(linkedListOne, linkedListTwo):
    one, two = linkedListOne, linkedListTwo
    while one is not two:
        one = one.next if one else linkedListTwo
        two = two.next if two else linkedListOne
    return one
