import heapq


# Algorithmic Beauty Bless You - O(e*logv) time | O(e+v) space
def primsAlgorithm(edges):
    mst = [[] for _ in edges]
    pqueue = [(w, 0, d) for d, w in edges[0]]
    heapq.heapify(pqueue)
    while pqueue:
        *_, d = popped = heapq.heappop(pqueue)
        if mst[d]:
            continue
        w, o, _ = popped
        mst[o].append([d, w])
        mst[d].append([o, w])
        for neighbor, w_nei in edges[d]:
            if not mst[neighbor]:
                heapq.heappush(pqueue, (w_nei, d, neighbor))
    return mst
