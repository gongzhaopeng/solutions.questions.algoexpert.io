# Algorithmic Beauty Bless You - O(nlogn) time | O(1) space
def minimumWaitingTime(queries):
    queries.sort()
    count = len(queries)
    return sum(map(lambda i: (count - 1 - i) * queries[i], range(count - 1)), 0)
