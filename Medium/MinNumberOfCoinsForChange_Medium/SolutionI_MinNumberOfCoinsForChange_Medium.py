# Algorithmic Beauty Bless You - O(nd) time | O(n) space
def minNumberOfCoinsForChange(n, denoms):
    dpt = [-1] * (n + 1)
    dpt[0] = 0
    for d in denoms:
        for amt in range(d, n + 1):
            if dpt[amt - d] >= 0 and (dpt[amt] < 0 or dpt[amt] > dpt[amt - d] + 1):
                dpt[amt] = dpt[amt - d] + 1
    return dpt[-1]
