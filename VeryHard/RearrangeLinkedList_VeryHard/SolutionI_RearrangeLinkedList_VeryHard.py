# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Algorithmic Beauty Bless You - O(n) time | O(1) space
def rearrangeLinkedList(head, k):
    less_head = less_tail = equal_head = equal_tail = greater_head = greater_tail = None
    current = head
    while current:
        if current.value < k:
            less_head, less_tail = update_sub_list(less_head, less_tail, current)
        elif current.value > k:
            greater_head, greater_tail = update_sub_list(greater_head, greater_tail, current)
        else:
            equal_head, equal_tail = update_sub_list(equal_head, equal_tail, current)
        current = current.next
    if less_head:
        head, tail = less_head, less_tail
    elif equal_head:
        head, tail = equal_head, equal_tail
    else:
        head, tail = greater_head, greater_tail
    if equal_tail and equal_tail is not tail:
        tail.next, tail = equal_head, equal_tail
    if greater_tail and greater_tail is not tail:
        tail.next, tail = greater_head, greater_tail
    tail.next = None
    return head


def update_sub_list(head, tail, new_node):
    if not head:
        return new_node, new_node
    tail.next = new_node
    return head, new_node
