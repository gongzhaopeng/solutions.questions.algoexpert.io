# Algorithmic Beauty Bless You - O(nd) time | O(n) space
def minNumberOfCoinsForChange(n, denoms):
    dpt = [float('inf')] * (n + 1)
    dpt[0] = 0
    for d in denoms:
        for amt in range(d, n + 1):
            dpt[amt] = min(dpt[amt], dpt[amt - d] + 1)
    return dpt[-1] if dpt[-1] != float('inf') else -1
