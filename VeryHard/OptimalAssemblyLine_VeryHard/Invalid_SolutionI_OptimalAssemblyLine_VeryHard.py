from dataclasses import dataclass, field
from typing import Any
import heapq


# ------ Invalid Solution ------
# Algorithmic Beauty Bless You - O(s+(s-n)*log(s)) time | O(s) space
def optimalAssemblyLine(stepDurations, numStations):
    if len(stepDurations) == 1:
        return stepDurations[0]
    min_heap, pre = [], Node(-1, -1)
    for i in range(len(stepDurations) - 1):
        node = Node(stepDurations[i], stepDurations[i] + stepDurations[i + 1])
        pre.next, node.pre, pre = node, pre, node
        min_heap.append(node)
    min_heap.append(Node(stepDurations[-1], float('inf')))
    min_heap[0].pre, min_heap[-2].next = None, min_heap[-1]
    heapq.heapify(min_heap)
    for _ in range(len(stepDurations) - numStations):
        while True:
            popped = heapq.heappop(min_heap)
            if not popped.removed:
                break
        pre, ne = popped.pre, popped.next
        popped.duration, popped.comb_duration = popped.comb_duration, popped.duration + ne.comb_duration
        heapq.heappush(min_heap, popped)
        if pre:
            new_pre = Node(pre.duration, pre.duration + popped.duration)
            pre.removed, new_pre.next, popped.pre = True, popped, new_pre
            heapq.heappush(min_heap, new_pre)
            if pre.pre:
                pre.pre.next, new_pre.pre = new_pre, pre.pre
        ne.removed, popped.next = True, ne.next
        if ne.next:
            ne.next.pre = popped
    return max(_.duration for _ in min_heap if not _.removed)


@dataclass(order=True)
class Node:
    duration: int = field(compare=False)
    comb_duration: Any
    pre: Any = field(compare=False, init=False, default=None)
    next: Any = field(compare=False, init=False, default=None)
    removed: bool = field(compare=False, init=False, default=False)
