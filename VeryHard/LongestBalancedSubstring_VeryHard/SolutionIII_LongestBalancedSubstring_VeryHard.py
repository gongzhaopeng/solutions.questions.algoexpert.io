# Algorithmic Beauty Bless You - O(n) time | O(1) space
def longestBalancedSubstring(string):
    return max(single_direction_check(string, '('),
               single_direction_check(reversed(string), ')'))


def single_direction_check(ch_seq, opening_ch):
    longest_len, opening_count, closing_count = 0, 0, 0
    for ch in ch_seq:
        if ch == opening_ch:
            opening_count += 1
            continue
        closing_count += 1
        if opening_count == closing_count:
            longest_len = max(longest_len, closing_count * 2)
        elif closing_count > opening_count:
            opening_count = closing_count = 0
    return longest_len
