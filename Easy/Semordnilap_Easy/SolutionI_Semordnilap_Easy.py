# Algorithmic Beauty Bless You - O(n*m) time | O(n*m) space
def semordnilap(words):
    pairs, registry = [], set()
    for w in words:
        rev = w[::-1]
        if rev in registry:
            pairs.append([rev, w])
        else:
            registry.add(w)
    return pairs
