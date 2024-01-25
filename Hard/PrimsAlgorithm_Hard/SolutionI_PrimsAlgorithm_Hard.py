import heapq


# Algorithmic Beauty Bless You - O(e*logv) time | O(e+v) space
def primsAlgorithm(edges):
    mst = [[] for _ in edges]
    pqueue = [[float('inf'), v, None, False] for v in range(len(edges))]
    entries = dict(enumerate(pqueue))
    while True:
        while pqueue:
            *_, removed = popped = heapq.heappop(pqueue)
            if not removed:
                break
        else:
            break
        w, v, p, _ = popped
        if p is not None:
            mst[v].append([p, w])
            mst[p].append([v, w])
        for neighbor, w in edges[v]:
            if mst[neighbor]:
                continue
            old_w, *_ = old_entry = entries[neighbor]
            if old_w > w:
                old_entry[-1] = True
                entries[neighbor] = new_entry = [w, neighbor, v, False]
                heapq.heappush(pqueue, new_entry)
    return mst
