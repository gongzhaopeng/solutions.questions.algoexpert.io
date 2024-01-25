# Algorithmic Beauty Bless You - O(d*s*t) time | O(t) space
def diceThrows(numDice, numSides, target):
    pre_dpt = [0] * (target + 1)
    cur_dpt = pre_dpt.copy()
    pre_dpt[0] = 1
    for _ in range(numDice):
        for t in range(target + 1):
            cur_dpt[t] = 0
            for side in range(1, min(t, numSides) + 1):
                cur_dpt[t] += pre_dpt[t - side]
        pre_dpt, cur_dpt = cur_dpt, pre_dpt
    return pre_dpt[target]
