# Algorithmic Beauty Bless You - O(n+m) time | O(c) space
def generateDocument(characters, document):
    src_counts = {}
    for c in characters:
        src_counts.setdefault(c, 0)
        src_counts[c] += 1
    for c in document:
        remain = src_counts.get(c) or 0
        if remain == 0:
            return False
        src_counts[c] -= 1
    return True
