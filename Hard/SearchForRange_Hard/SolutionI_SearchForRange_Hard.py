import math


# Algorithmic Beauty Bless You - O(logn) time | O(1) space
def searchForRange(array, target):
    occur_range = [-1, -1]
    occur_range[0] = binary_search_left(array, 0, len(array) - 1, target)
    if occur_range[0] >= 0:
        occur_range[1] = binary_search_right(array, occur_range[0], len(array) - 1, target)
    return occur_range


def binary_search_left(array, p_left, p_right, target):
    while p_left < p_right:
        p_mid = (p_left + p_right) // 2
        if target > array[p_mid]:
            p_left = p_mid + 1
        else:
            p_right = p_mid
    return p_left if target == array[p_left] else -1


def binary_search_right(array, p_left, p_right, target):
    while p_left < p_right:
        p_mid = math.ceil((p_left + p_right) / 2)
        if target < array[p_mid]:
            p_right = p_mid - 1
        else:
            p_left = p_mid
    return p_right if target == array[p_right] else -1
