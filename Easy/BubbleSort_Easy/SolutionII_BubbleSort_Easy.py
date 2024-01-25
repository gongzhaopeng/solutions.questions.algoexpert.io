# Algorithmic Beauty Bless You - O(n^2) time | O(1) space
def bubbleSort(array):
    max_index, is_sorted, count = len(array) - 1, False, 0
    while not is_sorted:
        is_sorted = True
        for i in range(max_index - count):
            if array[i] > array[i + 1]:
                array[i], array[i + 1], is_sorted = array[i + 1], array[i], False
        count += 1
    return array
