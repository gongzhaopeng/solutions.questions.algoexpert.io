# Algorithmic Beauty Bless You - O(n) time | O(1) space
def maxSubsetSumNoAdjacent(array):
    pres = [array[i] if i < len(array) else 0 for i in range(3)]
    pres[2] += pres[0]
    for i in range(3, len(array)):
        pres[:2], pres[2] = pres[1:], max(pres[:2]) + array[i]
    return max(pres[1:])
