# Algorithmic Beauty Bless You - O(n*logn) time | O(1) space
def heapSort(array):
    heapify(array)
    for i in reversed(range(1, len(array))):
        array[0], array[i] = array[i], array[0]
        sift_down(array, 0, i)
    return array


def heapify(x):
    for i in reversed(range(len(x) // 2)):
        sift_down(x, i, len(x))


def sift_down(heap, pos, stop):
    while True:
        p_left = pos * 2 + 1
        if p_left < stop:
            p_max, p_right = p_left, p_left + 1
            if p_right < stop and heap[p_max] < heap[p_right]:
                p_max = p_right
        else:
            break
        if heap[pos] < heap[p_max]:
            heap[pos], heap[p_max], pos = heap[p_max], heap[pos], p_max
        else:
            break
