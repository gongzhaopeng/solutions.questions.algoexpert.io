def nonConstructibleChange(coins):
    min_unable_change = 1
    coins.sort()
    for coin in coins:
        if coin > min_unable_change:
            break
        min_unable_change += coin
    return min_unable_change
