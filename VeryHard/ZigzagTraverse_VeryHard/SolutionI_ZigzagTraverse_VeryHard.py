def zigzagTraverse(matrix):
    def traverse_diag(r, c):
        for _ in range(diag_span):
            zigzag.append(matrix[r][c])
            r += step
            c -= step

    zigzag = []
    dim_diff = len(matrix) - len(matrix[0])
    if dim_diff > 0:
        min_dim = len(matrix[0])
    else:
        min_dim, dim_diff = len(matrix), -dim_diff
    step, start_i, start_j, i_plus_j, diag_span = 1, 0, 0, 0, 1
    for _ in range(0, min_dim - 1):
        traverse_diag(start_i, start_j)
        step = -step
        i_plus_j += 1
        diag_span += 1
        start_i, start_j = (0, i_plus_j) if step > 0 else (i_plus_j, 0)
    for _ in range(0, dim_diff + 1):
        traverse_diag(start_i, start_j)
        step = -step
        i_plus_j += 1
        if min_dim == len(matrix):
            start_i, start_j = (0, i_plus_j) if step > 0 else (min_dim - 1, i_plus_j - min_dim + 1)
        else:
            start_i, start_j = (i_plus_j - min_dim + 1, min_dim - 1) if step > 0 else (i_plus_j, 0)
    diag_span = min_dim - 1
    for _ in range(0, min_dim - 1):
        if step > 0:
            start_j = len(matrix[0]) - 1
            start_i = i_plus_j - start_j
        else:
            start_i = len(matrix) - 1
            start_j = i_plus_j - start_i
        traverse_diag(start_i, start_j)
        step = -step
        i_plus_j += 1
        diag_span -= 1
    return zigzag
