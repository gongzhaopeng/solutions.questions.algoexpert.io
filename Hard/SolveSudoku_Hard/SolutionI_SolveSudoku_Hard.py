# Algorithmic Beauty Bless You - O(1) time | O(1) space
def solveSudoku(board):
    rows = [[False] * 10 for _ in range(9)]
    columns = [[False] * 10 for _ in range(9)]
    squares = [[[False] * 10 for _ in range(3)] for _ in range(3)]
    flags = (rows, columns, squares)
    blanks = []
    for j in range(9):
        for i in range(9):
            square_i, square_j = i // 3, j // 3
            coord = (i, j, square_i, square_j)
            num = board[i][j]
            if num == 0:
                blanks.append((i, j, square_i, square_j))
            else:
                update_flag(flags, coord, num, True)
    p_cur = 0
    while p_cur < len(blanks):
        blank_i, blank_j, *_ = coord = blanks[p_cur]
        old_num = board[blank_i][blank_j]
        if old_num > 0:
            board[blank_i][blank_j] = 0
            update_flag(flags, coord, old_num, False)
        for new_num in range(old_num + 1, 10):
            if is_flagged(flags, coord, new_num):
                continue
            board[blank_i][blank_j] = new_num
            update_flag(flags, coord, new_num, True)
            break
        else:
            p_cur -= 2
        p_cur += 1
    return board


def update_flag(flags, coord, num, new_flag):
    flags[0][coord[0]][num] = new_flag
    flags[1][coord[1]][num] = new_flag
    flags[2][coord[2]][coord[3]][num] = new_flag


def is_flagged(flags, coord, num):
    return flags[0][coord[0]][num] or flags[1][coord[1]][num] or flags[2][coord[2]][coord[3]][num]
