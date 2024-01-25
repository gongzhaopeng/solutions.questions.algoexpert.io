# Algorithmic Beauty Bless You - O(n) time | O(1) space
def findThreeLargestNumbers(array):
    heap = [float('-inf')] * 3
    for num in array:
        if num <= heap[0]:
            continue
        heap[0] = num
        p_min = min(range(3), key=lambda _: heap[_])
        if p_min != 0:
            heap[0], heap[p_min] = heap[p_min], heap[0]
    if heap[1] > heap[2]:
        heap[1], heap[2] = heap[2], heap[1]
    return heap
