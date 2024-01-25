import heapq


# Algorithmic Beauty Bless You - O(n*logk) time | O(k) space
def sortKSortedArray(array, k):
    min_heap, i = array[:k], -1
    heapq.heapify(min_heap)
    for i in range(len(array) - k):
        heapq.heappush(min_heap, array[i + k])
        array[i] = heapq.heappop(min_heap)
    for j in range(i + 1, len(array)):
        array[j] = heapq.heappop(min_heap)
    return array
