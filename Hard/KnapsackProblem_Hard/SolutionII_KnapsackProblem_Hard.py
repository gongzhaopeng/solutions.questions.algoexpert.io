# Algorithmic Beauty Bless You - O(n * c) time | O(n * c) space
def knapsackProblem(items, capacity):
    dp_table = [[None for _ in range(len(items) + 1)] for _ in range(capacity + 1)]
    return [compute_max_value(capacity, len(items), dp_table, items),
            collect_picked_items(dp_table, items)]


def compute_max_value(c, i, dp_table, items):
    if c < 1 or i < 1:
        return 0
    if dp_table[c][i] is not None:
        return dp_table[c][i]
    max_value = compute_max_value(c, i - 1, dp_table, items)
    value, weight = items[i - 1]
    if weight <= c:
        max_value = max(max_value, compute_max_value(c - weight, i - 1, dp_table, items) + value)
    if max_value > 0:
        dp_table[c][i] = max_value
    return max_value


def collect_picked_items(dp_table, items):
    picked_items = []
    c, i = len(dp_table) - 1, len(items)
    while c > 0 and i > 0:
        if dp_table[c][i] is None:
            break
        if dp_table[c][i] != dp_table[c][i - 1]:
            picked_items.append(i - 1)
            c = c - items[i - 1][1]
        i -= 1
    picked_items.reverse()
    return picked_items
