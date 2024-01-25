# Algorithmic Beauty Bless You - O(v+e) time | O(v) space
def twoColorable(edges):
    colors, stack = [0] * len(edges), [0]
    colors[0] = -1
    while stack:
        v = stack.pop()
        for dest in edges[v]:
            if colors[dest] == colors[v]:
                return False
            elif colors[dest] == 0:
                colors[dest] = -colors[v]
                stack.append(dest)
    return True
