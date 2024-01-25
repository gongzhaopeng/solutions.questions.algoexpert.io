# Algorithmic Beauty Bless You - O(nlogn) time | O(1) space
def minimumWaitingTime(queries):
    queries.sort()
    return sum((i * q for i, q in enumerate(reversed(queries))))
