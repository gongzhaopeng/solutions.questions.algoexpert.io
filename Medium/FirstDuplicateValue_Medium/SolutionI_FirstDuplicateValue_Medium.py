# Algorithmic Beauty Bless You - O(n) time | O(1) space
def firstDuplicateValue(array):
    for e in array:
        index = abs(e) - 1
        if array[index] < 0:
            return index + 1
        array[index] = -array[index]
    return -1
