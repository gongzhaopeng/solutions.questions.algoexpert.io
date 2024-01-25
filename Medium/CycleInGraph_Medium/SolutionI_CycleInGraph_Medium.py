# Algorithmic Beauty Bless You - O(v+e) time | O(v) space
def cycleInGraph(edges):
    status = [0] * len(edges)
    for i in range(len(edges)):
        if checkCycleFrom(i, edges, status):
            return True
    return False


def checkCycleFrom(origin, edges, status):
    if status[origin] == 2:
        return False
    current, stack = [origin, 0], []
    while True:
        if current:
            vertex, _ = current
            if status[vertex] == 1:
                return True
            elif status[vertex] == 2:
                current = None
                continue
            status[vertex] = 1
            stack.append(current)
            current = [edges[vertex][0], 0] if edges[vertex] else None
        elif stack:
            stack[-1][1] += 1
            vertex, p_visiting = stack[-1]
            if p_visiting < len(edges[vertex]):
                current = [edges[vertex][p_visiting], 0]
                continue
            stack.pop()
            status[vertex] = 2
        else:
            return False
