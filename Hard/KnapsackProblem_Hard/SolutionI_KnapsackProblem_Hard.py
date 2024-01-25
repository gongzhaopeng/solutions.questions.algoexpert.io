# Algorithmic Beauty Bless You - O(n * c) time | O(n * c) space
def knapsackProblem(items, capacity):
    dp_table = [[0 for _ in range(len(items) + 1)] for _ in range(capacity + 1)]
    for c in range(1, capacity + 1):
        for i in range(1, len(items) + 1):
            dp_table[c][i] = dp_table[c][i - 1]
            value, weight = items[i - 1]
            if weight > c:
                continue
            dp_table[c][i] = max(dp_table[c][i], dp_table[c - weight][i - 1] + value)
    return [dp_table[-1][-1], collect_picked_items(dp_table, items)]


def collect_picked_items(dp_table, items):
    picked_items = []
    c, i = len(dp_table) - 1, len(items)
    while c > 0 and i > 0:
        if dp_table[c][i] != dp_table[c][i - 1]:
            picked_items.append(i - 1)
            c = c - items[i - 1][1]
        i -= 1
    picked_items.reverse()
    return picked_items
