import heapq
from dataclasses import dataclass, field
from typing import Any


@dataclass(order=True, frozen=True)
class GridInfo:
    f: int
    g: int
    h: int = field(compare=False)
    row: int = field(compare=False)
    col: int = field(compare=False)
    pre: Any = field(compare=False, default=None)
    removed: bool = field(compare=False, default=False)


# Algorithmic Beauty Bless You - O(h*wlog(h*w)) time | O(h*w) space
def aStarAlgorithm(startRow, startCol, endRow, endCol, graph):
    max_row, max_col = len(graph) - 1, len(graph[0]) - 1
    start_h = calc_h_value(startRow, startCol, endRow, endCol)
    pqueue = [GridInfo(start_h, 0, start_h, startRow, startCol)]
    heapq.heapify(pqueue)
    frontiers = {(e.row, e.col): e for e in pqueue}
    explored = set()
    while True:
        while pqueue:
            to_explore = heapq.heappop(pqueue)
            if not to_explore.removed:
                break
        else:
            break
        if to_explore.row == endRow and to_explore.col == endCol:
            return build_path(to_explore)
        del frontiers[(to_explore.row, to_explore.col)]
        explored.add((to_explore.row, to_explore.col))
        neighbors = collect_neighbors(to_explore.row, to_explore.col, max_row, max_col)
        for r, c in neighbors:
            if graph[r][c] == 1:
                continue
            if (r, c) in explored:
                continue
            neighbor_new_g = to_explore.g + 1
            neighbor_old_info = frontiers.get((r, c))
            if neighbor_old_info and neighbor_old_info.g <= neighbor_new_g:
                continue
            if neighbor_old_info:
                neighbor_h = neighbor_old_info.h
                neighbor_old_info.removed = True
            else:
                neighbor_h = calc_h_value(r, c, endRow, endCol)
            neighbor_new_info = GridInfo(neighbor_new_g + neighbor_h, neighbor_new_g,
                                         neighbor_h, r, c, to_explore)
            frontiers[(r, c)] = neighbor_new_info
            heapq.heappush(pqueue, neighbor_new_info)
    return []


def collect_neighbors(row, col, max_row, max_col):
    neighbors = []
    if row > 0:
        neighbors.append((row - 1, col))
    if row < max_row:
        neighbors.append((row + 1, col))
    if col > 0:
        neighbors.append((row, col - 1))
    if col < max_col:
        neighbors.append((row, col + 1))
    return neighbors


def calc_h_value(row, col, dest_row, dest_col):
    return abs(dest_row - row) + abs(dest_col - col)


def build_path(tail_node):
    path = []
    while tail_node:
        path.append([tail_node.row, tail_node.col])
        tail_node = tail_node.pre
    path.reverse()
    return path
