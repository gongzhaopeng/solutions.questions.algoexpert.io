# Algorithmic Beauty Bless You - O(n) time | O(1) space
def maxSubsetSumNoAdjacent(array):
    pres = [array[i] if i < len(array) else 0 for i in range(2)]
    pres[1] = max(pres)
    for i in range(2, len(array)):
        pres[0], pres[1] = pres[1], max(pres[1], pres[0] + array[i])
    return max(pres)
