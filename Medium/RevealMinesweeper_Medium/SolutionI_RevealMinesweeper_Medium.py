# Algorithmic Beauty Bless You - O(w*h) time | O(w*h) space
def revealMinesweeper(board, row, column):
    if board[row][column] == 'M':
        board[row][column] = 'X'
        return board
    board[row][column], stack = 0, [(row, column)]
    while stack:
        row, column = stack.pop()
        h_neighbors = []
        for r, c in collect_neighbors(row, column, board):
            if board[r][c] == 'M':
                board[row][column] += 1
            elif board[r][c] == 'H':
                h_neighbors.append((r, c))
        if board[row][column] == 0:
            for r, c in h_neighbors:
                stack.append((r, c))
                board[r][c] = 0
        board[row][column] = str(board[row][column])
    return board


def collect_neighbors(row, column, board):
    steps = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    return ((r, c) for r, c in map(lambda _: (_[0] + row, _[1] + column), steps)
            if -1 < r < len(board) and -1 < c < len(board[0]))
