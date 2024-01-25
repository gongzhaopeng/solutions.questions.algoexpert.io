# Algorithmic Beauty Bless You - O(n^2) time | O(1) space
def selectionSort(array):
    for i in range(len(array) - 1):
        p_min = min(range(i, len(array)), key=lambda _: array[_])
        array[i], array[p_min] = array[p_min], array[i]
    return array
