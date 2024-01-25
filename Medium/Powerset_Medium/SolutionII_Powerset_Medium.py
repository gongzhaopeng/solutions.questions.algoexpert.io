# Algorithmic Beauty Bless You - O(n*2^n) time | O(n*2^n) space
def powerset(array):
    sets = [[]]
    for e in array:
        for i in range(len(sets)):
            sets.append(sets[i] + [e])
    return sets
