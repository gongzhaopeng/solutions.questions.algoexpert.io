# Algorithmic Beauty Bless You - O(n * m) time | O(n * m) space
def longestCommonSubsequence(str1, str2):
    pre_row, cur_row = [[0, -1, None] for _ in range(len(str2) + 1)], None
    for i in range(1, len(str1) + 1):
        cur_row = [[0, -1, None] for _ in range(len(str2) + 1)]
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                cur_row[j][:2] = [pre_row[j - 1][0] + 1, i - 1]
                if pre_row[j - 1][0] > 0:
                    cur_row[j][2] = pre_row[j - 1]
            elif cur_row[j - 1][0] > pre_row[j][0]:
                cur_row[j] = cur_row[j - 1]
            else:
                cur_row[j] = pre_row[j]
        pre_row = cur_row
    subseq = []
    if cur_row:
        cur_grid = cur_row[-1] if cur_row[-1][0] > 0 else None
        while cur_grid:
            subseq.append(str1[cur_grid[1]])
            cur_grid = cur_grid[-1]
        subseq.reverse()
    return subseq
