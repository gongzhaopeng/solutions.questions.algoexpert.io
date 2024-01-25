# Algorithmic Beauty Bless You - O(n^2) time | O(n) space
def minNumberOfJumps(array):
    min_jumps = list(range(len(array)))
    for i in range(1, len(array)):
        for j in range(i):
            if array[j] >= i - j and min_jumps[j] + 1 < min_jumps[i]:
                min_jumps[i] = min_jumps[j] + 1
    return min_jumps[-1]
