# Algorithmic Beauty Bless You - O(wn) time | O(c) space
def minimumCharactersForWords(words):
    max_counts, min_chars = {}, []
    for word in words:
        counts = {}
        for ch in word:
            max_counts.setdefault(ch, 0)
            counts.setdefault(ch, 0)
            counts[ch] += 1
            if counts[ch] > max_counts[ch]:
                min_chars.append(ch)
                max_counts[ch] += 1
    return min_chars
