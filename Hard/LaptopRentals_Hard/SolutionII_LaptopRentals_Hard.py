import heapq
import operator


# Algorithmic Beauty Bless You - O(nlogn) time | O(n) space
def laptopRentals(times):
    times.sort(key=operator.itemgetter(0))
    rented = []
    for start, end in times:
        if rented and rented[0] <= start:
            heapq.heappop(rented)
        heapq.heappush(rented, end)
    return len(rented)
