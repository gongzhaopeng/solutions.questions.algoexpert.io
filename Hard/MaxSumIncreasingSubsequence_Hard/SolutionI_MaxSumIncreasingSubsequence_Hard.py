# Algorithmic Beauty Bless You - O(n^2) time | O(n) space
def maxSumIncreasingSubsequence(array):
    p_max_tail, stats = 0, [[num, -1] for num in array]
    for i in range(1, len(array)):
        for j in range(i):
            if array[i] > array[j]:
                candi_sum = stats[j][0] + array[i]
                if candi_sum > stats[i][0]:
                    stats[i][:] = [candi_sum, j]
        if stats[i][0] > stats[p_max_tail][0]:
            p_max_tail = i
    ret = [stats[p_max_tail][0], []]
    while p_max_tail >= 0:
        ret[-1].append(array[p_max_tail])
        p_max_tail = stats[p_max_tail][1]
    ret[-1].reverse()
    return ret
