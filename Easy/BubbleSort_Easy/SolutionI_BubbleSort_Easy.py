# Algorithmic Beauty Bless You - O(n^2) time | O(1) space
def bubbleSort(array):
    max_index = len(array) - 1
    for i in range(max_index):
        for j in range(max_index - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
