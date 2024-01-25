# Algorithmic Beauty Bless You - O(d*s*t) time | O(t) space
def diceThrows(numDice, numSides, target):
    target = target - numDice
    if target < 0:
        return 0
    achieved = [0, 0]
    pre_dpt = [0] * (target + 1)
    pre_dpt[0] = 1
    cur_dpt = pre_dpt.copy()
    for r in range(numDice):
        round_remain = numDice - 1 - r
        max_future_achieved = round_remain * (numSides - 1)
        new_achieved = [
            max(0, target - max_future_achieved),
            min(target, achieved[1] + numSides - 1)
        ]
        if new_achieved[0] > new_achieved[1]:
            break
        for t in range(new_achieved[0], new_achieved[1] + 1):
            cur_dpt[t] = 0
        for t in range(achieved[0], achieved[1] + 1):
            for side in range(max(new_achieved[0] - t, 0), min(new_achieved[1] - t, numSides - 1) + 1):
                cur_dpt[t + side] += pre_dpt[t]
        pre_dpt, cur_dpt, achieved = cur_dpt, pre_dpt, new_achieved
    return pre_dpt[-1]
