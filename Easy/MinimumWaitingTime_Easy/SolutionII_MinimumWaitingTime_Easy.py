# Algorithmic Beauty Bless You - O(nlogn) time | O(1) space
def minimumWaitingTime(queries):
    queries.sort()
    last_index = len(queries) - 1
    return sum((last_index - i) * queries[i] for i in range(last_index))
