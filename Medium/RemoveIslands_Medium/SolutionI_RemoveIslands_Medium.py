# Algorithmic Beauty Bless You - O(wh) time | O(wh) space
def removeIslands(matrix):
    visited = [False] * len(matrix[0])
    visited = [visited.copy() for _ in matrix]
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            remove_island(i, j, matrix, visited)
    return matrix


def remove_island(i, j, matrix, visited):
    if matrix[i][j] == 0 or visited[i][j]:
        return
    fields, visited[i][j], p_cur = [(i, j)], True, 0
    while p_cur < len(fields):
        (i, j), p_cur = fields[p_cur], p_cur + 1
        fields.extend(explore_unvisited_black_neighbors(i, j, matrix, visited))
    if any(map(lambda _: _[0] == 0 or _[0] == len(matrix) - 1 or _[1] == 0 or _[1] == len(matrix[0]) - 1,
               fields)):
        return
    for i, j in fields:
        matrix[i][j] = 0


def explore_unvisited_black_neighbors(i, j, matrix, visited):
    neighbors = []
    if i > 0:
        neighbors.append((i - 1, j))
    if i < len(matrix) - 1:
        neighbors.append((i + 1, j))
    if j > 0:
        neighbors.append((i, j - 1))
    if j < len(matrix[0]) - 1:
        neighbors.append((i, j + 1))
    neighbors = [(i, j) for (i, j) in neighbors if not visited[i][j] and matrix[i][j] == 1]
    for i, j in neighbors:
        visited[i][j] = True
    return neighbors
