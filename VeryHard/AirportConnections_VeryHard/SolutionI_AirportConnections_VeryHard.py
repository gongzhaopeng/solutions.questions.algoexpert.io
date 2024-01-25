# Algorithmic Beauty Bless You - O(a+r) time | O(a+r) space
def airportConnections(airports, routes, startingAirport):
    edges, v_start = transform_to_graph(airports, routes, startingAirport)
    markings = [None] * len(airports)
    mark_reachable(edges, v_start, markings)
    return count_joints(edges, markings)


def transform_to_graph(airports, routes, startingAirport):
    v_map = {mark: v for v, mark in enumerate(airports)}
    edges = [[] for _ in airports]
    for src, dest in routes:
        edges[v_map[src]].append(v_map[dest])
    return edges, v_map[startingAirport]


def mark_reachable(edges, v_start, markings):
    current, stack = [v_start, 0], []
    while True:
        if current:
            v, _ = current
            if markings[v] is not None:
                current = None
                continue
            stack.append(current)
            markings[v] = -1
            current = [edges[v][0], 0] if edges[v] else None
        elif stack:
            stack[-1][1] += 1
            v, p_visiting = stack[-1]
            if p_visiting < len(edges[v]):
                current = [edges[v][p_visiting], 0]
                continue
            stack.pop()
        else:
            break


def count_joints(edges, markings):
    joints = set()
    for cur_joint in range(len(markings)):
        if markings[cur_joint] is None:
            mark_from_joint(cur_joint, edges, joints, markings)
            joints.add(cur_joint)
    return len(joints)


def mark_from_joint(v_start, edges, joints, markings):
    current, stack = [v_start, 0], []
    while True:
        if current:
            v, _ = current
            if markings[v] is None:
                stack.append(current)
                markings[v] = -1
                current = [edges[v][0], 0] if edges[v] else None
                continue
            if markings[v] != -1:
                joints.remove(v)
            elif v == v_start:
                for v_in_cycle, _ in reversed(stack):
                    if markings[v_in_cycle] != v_start:
                        markings[v_in_cycle] = v_start
                    else:
                        break
            current = None
        elif stack:
            stack[-1][1] += 1
            v, p_visiting = stack[-1]
            if p_visiting < len(edges[v]):
                current = [edges[v][p_visiting], 0]
                continue
            stack.pop()
        else:
            break
    markings[v_start] = v_start
