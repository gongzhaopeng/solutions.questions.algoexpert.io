# Algorithmic Beauty Bless You - O(j+d) time | O(j+d) space
def topologicalSort(jobs, deps):
    topo_sorted, edges, dep_counts = [], {}, {}
    for p, d in deps:
        edges.setdefault(p, []).append(d)
        dep_counts[d] = dep_counts.setdefault(d, 0) + 1
    freed = [j for j in jobs if j not in dep_counts]
    while freed:
        topo_sorted.append(freed.pop())
        for d in edges.get(topo_sorted[-1], []):
            dep_counts[d] -= 1
            if dep_counts[d] == 0:
                freed.append(d)
    return topo_sorted if len(topo_sorted) == len(jobs) else []
