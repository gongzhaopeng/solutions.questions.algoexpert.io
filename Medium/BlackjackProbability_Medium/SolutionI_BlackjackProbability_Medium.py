# Algorithmic Beauty Bless You - O(t-s) time | O(1) space
def blackjackProbability(target, startingHand):
    diff = target - startingHand
    if diff < 5:
        return 0
    dpt, index = [0] * 5 + [0.5] + [1] * 5, 5
    for _ in range(6, diff + 1):
        index = _ % 11
        dpt[index] = dpt[index - 1] + (dpt[index - 1] - dpt[index]) / 10
    return round(dpt[index], 3)
