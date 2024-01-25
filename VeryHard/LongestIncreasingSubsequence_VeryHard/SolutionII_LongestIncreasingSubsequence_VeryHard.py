from bisect import bisect_left


# Algorithmic Beauty Bless You - O(nlogn) time | O(n) space
def longestIncreasingSubsequence(array):
    smallest_endings, endings_cnt, = [None] * len(array), 0
    seq_links = smallest_endings.copy()
    for i, num in enumerate(array):
        pos = bisect_left(smallest_endings, num, hi=endings_cnt, key=lambda _: array[_])
        if smallest_endings[pos] is None:
            endings_cnt = pos + 1
        if smallest_endings[pos] is None or array[smallest_endings[pos]] > num:
            smallest_endings[pos] = i
            if pos > 0:
                seq_links[i] = smallest_endings[pos - 1]
    longest_seq, current = [], smallest_endings[endings_cnt - 1]
    while current is not None:
        longest_seq.append(array[current])
        current = seq_links[current]
    longest_seq.reverse()
    return longest_seq
