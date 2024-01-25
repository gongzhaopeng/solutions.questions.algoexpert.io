# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Algorithmic Beauty Bless You - O(n) time | O(1) space
def findLoop(head):
    single_proceed = head.next
    double_proceed = single_proceed.next
    while single_proceed is not double_proceed:
        single_proceed = single_proceed.next
        double_proceed = double_proceed.next.next
    re_single_proceed = head
    while re_single_proceed is not single_proceed:
        re_single_proceed = re_single_proceed.next
        single_proceed = single_proceed.next
    return single_proceed
