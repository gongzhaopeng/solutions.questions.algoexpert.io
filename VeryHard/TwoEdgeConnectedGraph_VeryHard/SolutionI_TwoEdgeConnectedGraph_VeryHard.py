# Algorithmic Beauty Bless You - O(v+e) time | O(v) space
def twoEdgeConnectedGraph(edges):
    if len(edges) == 0:
        return True
    discovery_times, stack = [-1] * len(edges), []
    current = [0, -1, 0, -1]  # current = [v, v_parent, min_back_time, p_visiting]
    while True:
        if current:
            v, _, min_back_time, _ = current
            discovery_times[v] = min_back_time
            stack.append(current)
            current = discover_succession(current, discovery_times, edges)
        elif stack:
            current = discover_succession(stack[-1], discovery_times, edges)
            if current:
                continue
            v, _, min_back_time, _ = stack.pop()
            if not stack:
                break
            if discovery_times[v] == min_back_time:
                return False
            stack[-1][2] = min(stack[-1][2], min_back_time)
    return all(map(lambda _: _ != -1, discovery_times))


def discover_succession(current, discovery_times, edges):
    v, v_parent, _, p_visiting = current
    v_neighbors, succession = edges[v], None
    for p_visiting in range(p_visiting + 1, len(v_neighbors)):
        v_succession = v_neighbors[p_visiting]
        if discovery_times[v_succession] == -1:
            succession = [v_succession, v, discovery_times[v] + 1, -1]
            break
        elif v_succession != v_parent:
            current[2] = min(current[2], discovery_times[v_succession])
    current[-1] = p_visiting
    return succession
