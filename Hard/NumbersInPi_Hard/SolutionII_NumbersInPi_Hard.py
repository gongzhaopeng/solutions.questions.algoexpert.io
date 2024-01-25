import re
from collections import deque


# Algorithmic Beauty Bless You - O(n^2+nm) time | O(n^2) space
def numbersInPi(pi, numbers):
    edges = {}
    for num in numbers:
        for m in re.finditer(num, pi):
            edges.setdefault(m.start(), []).append(m.end())
    queue = deque([(0, 0)])
    while queue:
        start, depth = queue.popleft()
        for stop in edges.get(start, []):
            if stop == len(pi):
                return depth
            queue.append((stop, depth + 1))
    return -1
