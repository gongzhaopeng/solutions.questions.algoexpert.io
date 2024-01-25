# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Algorithmic Beauty Bless You - O(n) time | O(1) space
def linkedListPalindrome(head):
    single = double = head
    post_single = single.next
    while True:
        double = double.next
        if not double:
            single_forward, single_backward = post_single, single.next
            single.next, post_single = post_single, single
            break
        double = double.next
        if not double:
            single_forward, single_backward = post_single, single
            break
        post_single.next, post_single, single = single, post_single.next, post_single
    is_palindrome, head.next = True, None
    while single_forward:
        if single_forward.value != single_backward.value:
            is_palindrome = False
            break
        single_forward = single_forward.next
        single_backward.next, single_backward, post_single = post_single, single_backward.next, single_backward
    while single_backward:
        single_backward.next, single_backward, post_single = post_single, single_backward.next, single_backward
    return is_palindrome
