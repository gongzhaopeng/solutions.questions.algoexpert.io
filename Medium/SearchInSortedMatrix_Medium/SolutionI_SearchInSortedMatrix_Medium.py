# Algorithmic Beauty Bless You - O(m+n) time | O(1) space
def searchInSortedMatrix(matrix, target):
    i, j = 0, len(matrix[0]) - 1
    while i < len(matrix) and j > -1:
        if matrix[i][j] == target:
            return [i, j]
        elif matrix[i][j] > target:
            j -= 1
        else:
            i += 1
    return [-1, -1]
