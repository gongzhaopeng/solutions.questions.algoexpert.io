# Algorithmic Beauty Bless You - O(n^3+m) time | O(n+m) space
def numbersInPi(pi, numbers):
    dp_table = [float('inf')] * (len(pi) + 1)
    dp_table[0] = -1
    num_registry = set(numbers)
    for i in range(1, len(pi) + 1):
        for j in range(0, i):
            if pi[j:i] in num_registry:
                dp_table[i] = min(dp_table[i], dp_table[j] + 1)
    return dp_table[-1] if dp_table[-1] != float('inf') else -1
