# Algorithmic Beauty Bless You - O(h * w) time | O(h * w) space
def largestIsland(matrix):
    height, width = len(matrix), len(matrix[0])
    parents = [[None for _ in _] for _ in matrix]
    for r in range(height):
        for c in range(width):
            if matrix[r][c]:
                continue
            parents[r][c] = cur_root = [r, c, 0, 1]
            neighbor_roots = collect_neighbor_roots([r, c], parents)
            for neighbor_root in neighbor_roots:
                cur_root = union(cur_root, neighbor_root, parents)
    largest_size = 0
    for r in range(height):
        for c in range(width):
            if not matrix[r][c]:
                continue
            neighbor_roots = collect_neighbor_roots([r, c], parents)
            cur_size = 1
            for neighbor_root in neighbor_roots:
                cur_size += neighbor_root[-1]
            if cur_size > largest_size:
                largest_size = cur_size
    return largest_size


def collect_neighbor_roots(coord, parents):
    neighbor_coords = []
    if coord[0] > 0:
        neighbor_coords.append([coord[0] - 1, coord[1]])
    if coord[0] < len(parents) - 1:
        neighbor_coords.append([coord[0] + 1, coord[1]])
    if coord[1] > 0:
        neighbor_coords.append([coord[0], coord[1] - 1])
    if coord[1] < len(parents[0]) - 1:
        neighbor_coords.append([coord[0], coord[1] + 1])
    neighbor_roots = {}
    for coord in neighbor_coords:
        if parents[coord[0]][coord[1]]:
            root = find(coord, parents)
            neighbor_roots[id(root)] = root
    return list(neighbor_roots.values())


def find(coord, parents):
    p, path = parents[coord[0]][coord[1]], []
    while coord != p[:2]:
        path.append(coord)
        coord, p = p[:2], parents[p[0]][p[1]]
    for coord in path:
        parents[coord[0]][coord[1]] = p
    return p


def union(root_one, root_two, parents):
    rank_one, rank_two = root_one[2], root_two[2]
    if rank_one < rank_two:
        parents[root_one[0]][root_one[1]] = root_two
        root_two[-1] += root_one[-1]
        return root_two
    else:
        parents[root_two[0]][root_two[1]] = root_one
        root_one[-1] += root_two[-1]
        if rank_one == rank_two:
            root_one[2] += 1
        return root_one
