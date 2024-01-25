# Algorithmic Beauty Bless You - O(n^2) time | O(n) space
def longestPalindromicSubstring(string):
    longest = [0, 0]
    for i in range(1, len(string)):
        longest = search_longer_palindromic([i - 1, i], string, longest)
        longest = search_longer_palindromic([i, i], string, longest)
    return string[longest[0]:longest[1] + 1]


def search_longer_palindromic(origin, string, longest):
    while origin[0] > -1 and origin[1] < len(string) and string[origin[0]] == string[origin[1]]:
        origin[0], origin[1] = origin[0] - 1, origin[1] + 1
    origin[0], origin[1] = origin[0] + 1, origin[1] - 1
    return origin if origin[1] - origin[0] > longest[1] - longest[0] else longest
