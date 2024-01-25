# Algorithmic Beauty Bless You - O(n^2) time | O(n) space
def longestPalindromicSubstring(string):
    dpt, longest = [True] * len(string), [0, 0]
    for i in range(1, len(string)):
        for j in range(i):
            if string[i] != string[j]:
                dpt[j] = False
                continue
            dpt[j] = dpt[j + 1]
            if dpt[j] and i - j > longest[1] - longest[0]:
                longest = [j, i]
    return string[longest[0]:longest[1] + 1]
