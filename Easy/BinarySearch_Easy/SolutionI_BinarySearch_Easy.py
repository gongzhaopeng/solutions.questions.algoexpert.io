# Algorithmic Beauty Bless You - O(logn) time | O(1) space
def binarySearch(array, target):
    p_left, p_right = 0, len(array) - 1
    while p_left < p_right:
        p_mid = (p_left + p_right) // 2
        if target > array[p_mid]:
            p_left = p_mid + 1
        else:
            p_right = p_mid
    return p_left if target == array[p_left] else -1
