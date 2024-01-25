# Algorithmic Beauty Bless You - O(logn) time | O(1) space
def indexEqualsValue(array):
    p_head, p_tail = 0, len(array) - 1
    while p_head < p_tail:
        p_mid = (p_head + p_tail) // 2
        if array[p_mid] < p_mid:
            p_head = p_mid + 1
        else:
            p_tail = p_mid
    return p_head if array and array[p_head] == p_head else -1
