# Algorithmic Beauty Bless You - O(wh) time | O(wh) space
def minimumPassesOfMatrix(matrix):
    neg_amount, frontier = 0, []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] < 0:
                neg_amount = neg_amount + 1
            elif matrix[i][j] > 0:
                frontier.append((i, j))
    pass_num = 0
    while frontier:
        new_frontier = []
        for i, j in frontier:
            new_frontier.extend(convert_neg_neighbors(i, j, matrix))
        if not new_frontier:
            break
        pass_num, neg_amount, frontier = pass_num + 1, neg_amount - len(new_frontier), new_frontier
    return pass_num if neg_amount == 0 else -1


def convert_neg_neighbors(i, j, matrix):
    neighbors = []
    if i > 0:
        neighbors.append((i - 1, j))
    if i < len(matrix) - 1:
        neighbors.append((i + 1, j))
    if j > 0:
        neighbors.append((i, j - 1))
    if j < len(matrix[0]) - 1:
        neighbors.append((i, j + 1))
    neighbors = [(i, j) for i, j in neighbors if matrix[i][j] < 0]
    for i, j in neighbors:
        matrix[i][j] *= -1
    return neighbors
