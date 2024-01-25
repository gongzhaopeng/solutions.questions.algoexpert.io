# Algorithmic Beauty Bless You - O(n^2) time | O(n) space
def numberOfBinaryTreeTopologies(n):
    dpt = [0] * (n + 1)
    dpt[0] = 1
    for i in range(1, n + 1):
        mid = i // 2
        for j in range(0, mid):
            dpt[i] += dpt[j] * dpt[i - 1 - j] * 2
        if i % 2:
            dpt[i] += dpt[mid] * dpt[mid]
    return dpt[-1]
