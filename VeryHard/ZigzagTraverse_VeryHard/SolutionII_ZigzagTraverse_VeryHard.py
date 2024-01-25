import itertools


def zigzagTraverse(matrix):
    zigzag = []
    height, width = len(matrix), len(matrix[0])
    min_dim, dim_diff = (height, width - height) if height < width else (width, height - width)
    step, max_i, max_j = 1, height - 1, width - 1
    for diag_index, diag_span in enumerate(itertools.chain(range(1, min_dim + 1),
                                                           [min_dim for _ in range(dim_diff)],
                                                           reversed(range(1, min_dim)))):
        if step > 0:
            i, j = (0, diag_index) if diag_index < width else (diag_index - max_j, max_j)
        else:
            i, j = (diag_index, 0) if diag_index < height else (max_i, diag_index - max_i)
        for _ in range(diag_span):
            zigzag.append(matrix[i][j])
            i, j = i + step, j - step
        step = -step
    return zigzag
