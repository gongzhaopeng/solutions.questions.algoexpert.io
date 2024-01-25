# Algorithmic Beauty Bless You - O(logn) time | O(1) space
def shiftedBinarySearch(array, target):
    p_head, p_tail = 0, len(array) - 1
    while p_head < p_tail:
        p_mid = (p_head + p_tail) // 2
        if target > array[p_mid]:
            if target > array[p_tail]:
                if array[p_tail] > array[p_mid]:
                    p_tail = p_mid - 1
                else:
                    p_head, p_tail = p_mid + 1, p_tail - 1
            else:
                p_head = p_mid + 1
        else:
            if target < array[p_head]:
                if array[p_head] < array[p_mid]:
                    p_head = p_mid + 1
                else:
                    p_head, p_tail = p_head + 1, p_mid
            else:
                p_tail = p_mid
    return p_head if target == array[p_head] else -1
