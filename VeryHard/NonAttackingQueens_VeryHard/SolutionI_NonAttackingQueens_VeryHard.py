# Algorithmic Beauty Bless You - O(n!) time | O(n) space
def nonAttackingQueens(n):
    count, col_marks = 0, [False] * n
    slash_marks = [False] * (2 * n - 1)
    backslash_marks = slash_marks.copy()
    current, stack = [0, 0], [[None, 0]]
    while True:
        if current:
            row = len(stack) - 1
            col, _ = current
            i_slash, i_backslash = get_diag_indices(row, col, n)
            if col_marks[col] or slash_marks[i_slash] or backslash_marks[i_backslash]:
                current = None
                continue
            if row >= n - 1:
                count, current = count + 1, None
                continue
            col_marks[col] = slash_marks[i_slash] = backslash_marks[i_backslash] = True
            stack.append(current)
            current = [0, 0]
        elif stack:
            stack[-1][1] += 1
            col, next_col = stack[-1]
            if next_col < n:
                current = [next_col, 0]
                continue
            stack.pop()
            if col is None:
                break
            row = len(stack) - 1
            i_slash, i_backslash = get_diag_indices(row, col, n)
            col_marks[col] = slash_marks[i_slash] = backslash_marks[i_backslash] = False
        else:
            break
    return count


def get_diag_indices(row, col, n):
    return (n - 1) - (row - col), row + col
