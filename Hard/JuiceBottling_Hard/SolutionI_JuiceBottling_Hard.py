# Algorithmic Beauty Bless You - O(n^2) time | O(n^2) space
def juiceBottling(prices):
    db_table = [[0 for _ in range(len(prices))] for _ in range(len(prices))]
    for amt in range(1, len(prices)):
        for last_bottle in range(1, amt + 1):
            db_table[amt][last_bottle] = max(db_table[amt][last_bottle - 1],
                                             prices[last_bottle] +
                                             db_table[amt - last_bottle][min(amt - last_bottle, last_bottle)])
    return collect_bottles(db_table, len(prices) - 1)


def collect_bottles(db_table, amount):
    bottles = []
    last_bottle = amount
    while amount != 0:
        if db_table[amount][last_bottle] == db_table[amount][last_bottle - 1]:
            last_bottle -= 1
        else:
            bottles.append(last_bottle)
            amount = amount - last_bottle
            last_bottle = min(amount, last_bottle)
    bottles.reverse()
    return bottles
