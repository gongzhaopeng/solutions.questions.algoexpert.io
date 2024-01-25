# Algorithmic Beauty Bless You - O(n) time | O(min(n,a)) space
def longestSubstringWithoutDuplication(string):
    longest, chars, p_head = [0, 0], {}, 0
    for p_cur, ch in enumerate(string):
        p_dup = chars.get(ch)
        if p_dup is not None and p_dup >= p_head:
            if p_cur - p_head > longest[1] - longest[0]:
                longest = [p_head, p_cur]
            p_head = p_dup + 1
        chars[ch] = p_cur
    return string[longest[0]:longest[1]] if len(string) - p_head < longest[1] - longest[0] else string[p_head:]
