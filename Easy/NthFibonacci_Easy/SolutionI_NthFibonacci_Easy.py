# Algorithmic Beauty Bless You - O(n) time | O(1) space
def getNthFib(n):
    a, b = 0, 1
    if n == 1:
        return a
    elif n == 2:
        return b
    for _ in range(2, n):
        a, b = b, a + b
    return b
