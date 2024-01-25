# Algorithmic Beauty Bless You - O(n) time | O(1) space
def firstNonRepeatingCharacter(string):
    counts = {}
    for c in string:
        counts[c] = counts.get(c, 0) + 1
    return next((_ for _ in range(len(string)) if counts[string[_]] == 1), -1)
