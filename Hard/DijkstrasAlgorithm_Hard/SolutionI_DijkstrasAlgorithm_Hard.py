import heapq


# Algorithmic Beauty Bless You - O((v+e)log(v+e)) time | O(v+e) space
def dijkstrasAlgorithm(start, edges):
    distances = [-1] * len(edges)
    pqueue = [[float('inf'), i, False] for i in range(len(edges))]
    pqueue[start] = [0, start, False]
    unvisited = {i: e for i, e in enumerate(pqueue)}
    heapq.heapify(pqueue)
    while True:
        while pqueue:
            path_len, number, removed = heapq.heappop(pqueue)
            if not removed:
                break
        else:
            break
        if path_len == float('inf'):
            break
        distances[number] = path_len
        del unvisited[number]
        for dest, dis in edges[number]:
            entry = unvisited.get(dest)
            if not entry:
                continue
            new_neighbor_path_len = path_len + dis
            if new_neighbor_path_len < entry[0]:
                entry[-1] = True
                new_entry = [new_neighbor_path_len, dest, False]
                heapq.heappush(pqueue, new_entry)
                unvisited[dest] = new_entry
    return distances
