# Algorithmic Beauty Bless You - O(h*w) time | O(size*w) space
def maximumSumSubmatrix(matrix, size):
    height, width = len(matrix), len(matrix[0])
    db_table = [[0 for _ in range(width + 1)] for _ in range(size + 1)]
    max_sum = float('-inf')
    for i in range(height):
        r = i % (size + 1)
        for j in range(width):
            db_table[r][j] = db_table[r][j - 1] + db_table[r - 1][j] - db_table[r - 1][j - 1] + matrix[i][j]
            if i >= size - 1 and j >= size - 1:
                cur_sum = db_table[r][j] - db_table[r][j - size] - db_table[r - size][j] + db_table[r - size][j - size]
                if cur_sum > max_sum:
                    max_sum = cur_sum
    return max_sum
