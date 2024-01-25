# Algorithmic Beauty Bless You - O(h * w) time | O(h * w) space
def largestIsland(matrix):
    height, width = len(matrix), len(matrix[0])
    land_number, land_sizes = 2, {}
    for r in range(height):
        for c in range(width):
            land_size = mark_land_rooted_at(r, c, matrix, land_number)
            if land_size:
                land_sizes[land_number] = land_size
                land_number += 1
    largest_size = 0
    for r in range(height):
        for c in range(width):
            if matrix[r][c] != 1:
                continue
            land_numbers = set(map(lambda _: matrix[_[0]][_[1]], collect_neighbors(r, c, matrix)))
            largest_size = max(sum(map(lambda _: land_sizes.get(_, 0), land_numbers), 1),
                               largest_size)
    return largest_size


def mark_land_rooted_at(r, c, matrix, island_number):
    land_size, frontiers = 0, [[r, c]]
    while frontiers:
        r, c = frontiers.pop()
        if matrix[r][c] != 0:
            continue
        matrix[r][c] = island_number
        land_size += 1
        frontiers.extend(collect_neighbors(r, c, matrix))
    return land_size


def collect_neighbors(r, c, matrix):
    neighbors = []
    if r > 0:
        neighbors.append([r - 1, c])
    if r < len(matrix) - 1:
        neighbors.append([r + 1, c])
    if c > 0:
        neighbors.append([r, c - 1])
    if c < len(matrix[0]) - 1:
        neighbors.append([r, c + 1])
    return neighbors
