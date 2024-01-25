# Algorithmic Beauty Bless You - O(j+d) time | O(j+d) space
def topologicalSort(jobs, deps):
    topo_sorted = []
    rev_edges = {}
    for p, d in deps:
        rev_edges.setdefault(d, []).append(p)
    visit_indices = {}
    for job in jobs:
        visit_indices[job] = len(rev_edges.get(job, []))
    for job in jobs:
        stack, visiting, current = [], set(), job
        while True:
            if current is not None:
                index = visit_indices[current]
                if index < 0:
                    current = None
                    continue
                if current in visiting:
                    return []
                stack.append(current)
                visiting.add(current)
                if index > 0:
                    visit_indices[current] = index - 1
                    current = rev_edges[current][index - 1]
                else:
                    current = None
            elif stack:
                parent = stack[-1]
                index = visit_indices[parent] - 1
                visit_indices[parent] = index
                if index >= 0:
                    current = rev_edges[parent][index]
                else:
                    topo_sorted.append(parent)
                    stack.pop()
                    visiting.remove(parent)
                    current = None
            else:
                break
    return topo_sorted
