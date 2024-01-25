from bisect import bisect_left


# Algorithmic Beauty Bless You - O(nlogn) time | O(n) space
def longestIncreasingSubsequence(array):
    smallest_endings, endings_cnt, = [None] * len(array), 0
    seq_links, num_positions = smallest_endings.copy(), {}
    for i, num in enumerate(array):
        pos = bisect_left(smallest_endings, num, hi=endings_cnt)
        if smallest_endings[pos] is None:
            endings_cnt = pos + 1
        if smallest_endings[pos] is None or smallest_endings[pos] > num:
            smallest_endings[pos] = num
            if pos > 0:
                seq_links[i] = num_positions[smallest_endings[pos - 1]]
            num_positions[num] = i
    longest_seq = [smallest_endings[endings_cnt - 1]]
    pre = num_positions[longest_seq[-1]]
    while seq_links[pre] is not None:
        pre = seq_links[pre]
        longest_seq.append(array[pre])
    longest_seq.reverse()
    return longest_seq
