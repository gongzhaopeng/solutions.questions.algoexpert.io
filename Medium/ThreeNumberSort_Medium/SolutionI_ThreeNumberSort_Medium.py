# Algorithmic Beauty Bless You - O(n) time | O(1) space
def threeNumberSort(array, order):
    left, right, cur = 0, len(array) - 1, 0
    while cur <= right:
        if array[cur] == order[-1]:
            swap(cur, right, array)
            right -= 1
        elif array[cur] == order[0]:
            swap(cur, left, array)
            left, cur = left + 1, cur + 1
        else:
            cur += 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
