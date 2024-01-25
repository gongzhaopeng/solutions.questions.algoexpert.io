def zigzagTraverse(matrix):
    zigzag = []
    max_i, max_j = len(matrix) - 1, len(matrix[0]) - 1
    downward, i, j = True, 0, 0
    while i <= max_i and j <= max_j:
        zigzag.append(matrix[i][j])
        if downward:
            if i < max_i:
                if j > 0:
                    i, j = i + 1, j - 1
                else:
                    i += 1
                    downward = False
            else:
                j += 1
                downward = False
        else:
            if j < max_j:
                if i > 0:
                    i, j = i - 1, j + 1
                else:
                    j += 1
                    downward = True
            else:
                i += 1
                downward = True
    return zigzag
