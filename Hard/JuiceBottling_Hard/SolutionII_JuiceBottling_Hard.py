# Algorithmic Beauty Bless You - O(n^2) time | O(n) space
def juiceBottling(prices):
    profits = [0] * len(prices)
    head_bottles = profits.copy()
    profits[1], head_bottles[1] = prices[1], 1
    for amt in range(2, len(prices)):
        profits[amt], head_bottles[amt] = prices[amt], amt
        for head_bottle in range(1, amt // 2 + 1):
            p = prices[head_bottle] + profits[amt - head_bottle]
            if p > profits[amt]:
                profits[amt], head_bottles[amt] = p, head_bottle
    bottles, amt = [], len(prices) - 1
    while amt > 0:
        bottles.append(head_bottles[amt])
        amt -= head_bottles[amt]
    return bottles
