# Algorithmic Beauty Bless You - O(w*nlogn) time | O(wn) space
def groupAnagrams(words):
    registry = {}
    for word in words:
        registry.setdefault(''.join(sorted(word)), []).append(word)
    return list(registry.values())
