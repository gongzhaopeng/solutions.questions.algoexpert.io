# Algorithmic Beauty Bless You - O(wn) time | O(c) space
def minimumCharactersForWords(words):
    max_counts, min_chars = {}, []
    for word in words:
        counts = {}
        for ch in word:
            counts.setdefault(ch, 0)
            counts[ch] += 1
        for ch, count in counts.items():
            max_counts.setdefault(ch, 0)
            max_counts[ch] = max(max_counts[ch], count)
    for ch, count in max_counts.items():
        for _ in range(count):
            min_chars.append(ch)
    return min_chars
