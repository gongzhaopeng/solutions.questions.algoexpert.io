from collections import deque


# BFS, but not with the specified algorithm.
# Algorithmic Beauty Bless You - O(h * w) time | O(h * w) space
def aStarAlgorithm(startRow, startCol, endRow, endCol, graph):
    path = []
    max_row, max_col = len(graph) - 1, len(graph[0]) - 1
    queue, visited = deque([[startRow, startCol, None]]), {(startRow, startCol)}
    while queue:
        row, col, _ = current = queue.popleft()
        if row == endRow and col == endCol:
            break
        neighbors = []
        if row > 0:
            neighbors.append((row - 1, col))
        if row < max_row:
            neighbors.append((row + 1, col))
        if col > 0:
            neighbors.append((row, col - 1))
        if col < max_col:
            neighbors.append((row, col + 1))
        for r, c in neighbors:
            if graph[r][c] == 0 and (r, c) not in visited:
                queue.append([r, c, current])
                visited.add((r, c))
    else:
        current = None
    while current:
        path.append(current[:2])
        current = current[2]
    path.reverse()
    return path
