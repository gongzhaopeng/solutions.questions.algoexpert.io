import unittest


def riverSizes(matrix):
    def traverse_node():
        def get_unvisited_neighbors():
            unvisited_neighbors = []
            if ci > 0 and not visited[ci - 1][cj]:
                unvisited_neighbors.append([ci - 1, cj])
            if ci < len(matrix) - 1 and not visited[ci + 1][cj]:
                unvisited_neighbors.append([ci + 1, cj])
            if cj > 0 and not visited[ci][cj - 1]:
                unvisited_neighbors.append([ci, cj - 1])
            if cj < len(matrix[0]) - 1 and not visited[ci][cj + 1]:
                unvisited_neighbors.append([ci, cj + 1])
            return unvisited_neighbors

        current_river_size = 0
        nodes_to_explore = [[i, j]]
        while len(nodes_to_explore):
            current_node = nodes_to_explore.pop()
            ci = current_node[0]
            cj = current_node[1]
            if visited[ci][cj]:
                continue
            visited[ci][cj] = True
            if matrix[ci][cj] == 0:
                continue
            current_river_size += 1
            nodes_to_explore.extend(get_unvisited_neighbors())
        if current_river_size > 0:
            sizes.append(current_river_size)

    sizes = []
    visited = [[False for _ in row] for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverse_node()
    return sizes


class TestRiverSizes(unittest.TestCase):
    def test_case1(self):
        matrix = [
            [1, 0, 0, 1, 0],
            [1, 0, 1, 0, 0],
            [0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 0]
        ]
        target_sizes = [1, 2, 2, 2, 5]
        self.assertCountEqual(
            riverSizes(matrix),
            target_sizes
        )


if __name__ == '__main__':
    unittest.main()
