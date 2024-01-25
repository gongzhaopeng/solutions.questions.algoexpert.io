import operator


# Algorithmic Beauty Bless You - O(e*loge) time | O(e+v) space
def kruskalsAlgorithm(edges):
    mst = [[] for _ in edges]
    sorted_edges = []
    for o, row in enumerate(edges):
        for d, w in row:
            if o < d:
                sorted_edges.append([o, d, w])
    sorted_edges.sort(key=operator.itemgetter(-1))
    parents, ranks = {}, {}
    for v in range(len(edges)):
        parents[v], ranks[v] = v, 0
    for o, d, w in sorted_edges:
        o_root, d_root = find(o, parents), find(d, parents)
        if o_root == d_root:
            continue
        mst[o].append([d, w])
        mst[d].append([o, w])
        union(o_root, d_root, parents, ranks)
    return mst


def find(v, parents):
    p, path = parents[v], []
    while v != p:
        path.append(v)
        v, p = p, parents[p]
    for v in path:
        parents[v] = p
    return p


def union(root_one, root_two, parents, ranks):
    rank_one, rank_two = ranks[root_one], ranks[root_two]
    if rank_one < rank_two:
        parents[root_one] = root_two
    else:
        parents[root_two] = root_one
        if rank_one == rank_two:
            ranks[root_one] = rank_one + 1
