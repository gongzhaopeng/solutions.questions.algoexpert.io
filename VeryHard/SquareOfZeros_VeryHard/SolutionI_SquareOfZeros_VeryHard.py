# Algorithmic Beauty Bless You - O(n^3) time | O(n^2) space
def squareOfZeroes(matrix):
    height, width = len(matrix), len(matrix[0])
    grid_infos = [[(0, 0) for _ in range(width)] for _ in range(height)]
    if matrix[0][0] == 0:
        grid_infos[0][0] = (1, 1)
    for i in range(1, height):
        if matrix[i][0] == 0:
            grid_infos[i][0] = (grid_infos[i - 1][0][0] + 1, 1)
    for j in range(1, width):
        if matrix[0][j] == 0:
            grid_infos[0][j] = (1, grid_infos[0][j - 1][1] + 1)
    for i in range(1, height):
        for j in range(1, width):
            if matrix[i][j] == 0:
                grid_infos[i][j] = (grid_infos[i - 1][j][0] + 1, grid_infos[i][j - 1][1] + 1)
            max_square_size = min(grid_infos[i][j])
            for square_size in range(2, max_square_size + 1):
                hor_adj_end, ver_adj_end = grid_infos[i][j - square_size + 1], grid_infos[i - square_size + 1][j]
                if hor_adj_end[0] >= square_size and ver_adj_end[1] >= square_size:
                    return True
    return False
