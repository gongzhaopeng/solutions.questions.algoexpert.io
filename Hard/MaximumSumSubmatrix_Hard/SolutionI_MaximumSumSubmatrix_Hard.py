# Algorithmic Beauty Bless You - O(h*w) time | O(size*w) space
def maximumSumSubmatrix(matrix, size):
    height, width = len(matrix), len(matrix[0])
    db_table = [[[0, 0] for _ in range(width)] for _ in range(size)]
    max_sum = float('-inf')
    for i in range(height):
        row = i % size
        for j in range(width):
            old_sub_row_sum = db_table[row][j][0]
            db_table[row][j][0] = matrix[i][j]
            if j > 0:
                db_table[row][j][0] += db_table[row][j - 1][0]
            if j >= size:
                db_table[row][j][0] -= matrix[i][j - size]
            if j >= size - 1:
                db_table[row][j][1] = db_table[row - 1][j][1] + db_table[row][j][0]
                if i >= size:
                    db_table[row][j][1] -= old_sub_row_sum
            if i >= size - 1 and j >= size - 1 and db_table[row][j][1] > max_sum:
                max_sum = db_table[row][j][1]
    return max_sum
