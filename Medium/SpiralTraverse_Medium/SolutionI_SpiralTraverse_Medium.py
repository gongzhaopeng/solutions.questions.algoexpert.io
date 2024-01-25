# O(n*m) time | O(n*m) space - Algorithmic Beauty Bless You
def spiralTraverse(matrix):
    spiral = []
    j, i, step, j_span, i_span = -1, 0, 1, len(matrix[0]), len(matrix) - 1
    while True:
        if j_span < 1:
            break
        for _ in range(j_span):
            j += step
            spiral.append(matrix[i][j])
        j_span -= 1
        if i_span < 1:
            break
        for _ in range(i_span):
            i += step
            spiral.append(matrix[i][j])
        i_span -= 1
        step = -step
    return spiral
