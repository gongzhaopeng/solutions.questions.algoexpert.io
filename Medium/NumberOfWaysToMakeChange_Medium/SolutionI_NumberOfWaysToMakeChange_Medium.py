# Algorithmic Beauty Bless You - O(nd) time | O(n) space
def numberOfWaysToMakeChange(n, denoms):
    dpt = [0] * (n + 1)
    dpt[0] = 1
    for d in denoms:
        for amt in range(d, n + 1):
            dpt[amt] += dpt[amt - d]
    return dpt[-1]
