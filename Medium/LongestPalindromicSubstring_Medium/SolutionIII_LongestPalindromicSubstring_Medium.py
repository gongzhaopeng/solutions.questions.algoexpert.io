# Manacher's Algorithm: https://www.scaler.com/topics/data-structures/manachers-algorithm/
# Algorithmic Beauty Bless You - O(n) time | O(n) space
def longestPalindromicSubstring(string):
    length = 2 * len(string) + 3
    chars, p_cur = [0] * length, 2
    chars[0], chars[-1] = -1, -2
    for ch in string:
        chars[p_cur], p_cur = ch, p_cur + 2
    # string = 'abc' => chars = [-1, 'a', 0, 'b', 0, 'c', -2]
    longest_start, longest_len = 0, 0
    center, max_right, radius = 0, 0, [0] * length
    for i in range(1, length - 1):
        if i < max_right:
            i_mirror = center - (i - center)
            if radius[i_mirror] < max_right - i:
                radius[i] = radius[i_mirror]
                continue
            radius[i] = max_right - i
        while chars[i - radius[i] - 1] == chars[i + radius[i] + 1]:
            radius[i] += 1
        center, max_right = i, i + radius[i]
        if radius[i] > longest_len:
            longest_start, longest_len = (i - radius[i] - 1) // 2, radius[i]
    return string[longest_start:longest_start + longest_len]
