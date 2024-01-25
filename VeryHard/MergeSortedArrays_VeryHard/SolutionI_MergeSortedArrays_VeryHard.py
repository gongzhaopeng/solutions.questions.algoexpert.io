import heapq


# Algorithmic Beauty Bless You - O(nlogk) time | O(n) space
def mergeSortedArrays(arrays):
    merged = []
    min_heap = [(array[0], 0, array) for i, array in enumerate(arrays)]
    heapq.heapify(min_heap)
    while min_heap:
        minimum, i, array = heapq.heappop(min_heap)
        merged.append(minimum)
        i += 1
        if i < len(array):
            heapq.heappush(min_heap, (array[i], i, array))
    return merged
