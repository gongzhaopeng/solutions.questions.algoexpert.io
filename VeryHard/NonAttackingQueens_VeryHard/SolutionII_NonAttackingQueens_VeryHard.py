# Algorithmic Beauty Bless You - O(n!) time | O(n) space
def nonAttackingQueens(n):
    count, col_marks = 0, [False] * n
    slash_marks = [False] * (2 * n - 1)
    backslash_marks = slash_marks.copy()
    col, stack = 0, []
    while True:
        if col is not None:
            row = len(stack)
            while col < n:
                i_slash, i_backslash = get_diag_indices(row, col, n)
                if not col_marks[col] and not slash_marks[i_slash] and not backslash_marks[i_backslash]:
                    break
                col += 1
            else:
                col = None
                continue
            if row == n - 1:
                count, col = count + 1, None
                continue
            col_marks[col] = slash_marks[i_slash] = backslash_marks[i_backslash] = True
            stack.append(col)
            col = 0
        elif stack:
            col = stack.pop()
            row = len(stack)
            i_slash, i_backslash = get_diag_indices(row, col, n)
            col_marks[col] = slash_marks[i_slash] = backslash_marks[i_backslash] = False
            col += 1
        else:
            break
    return count


def get_diag_indices(row, col, n):
    return (n - 1) - (row - col), row + col
