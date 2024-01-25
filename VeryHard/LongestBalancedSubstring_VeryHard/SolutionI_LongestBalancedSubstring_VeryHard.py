# Algorithmic Beauty Bless You - O(n) time | O(n) space
def longestBalancedSubstring(string):
    longest_len, stack = 0, [['$', 0]]
    for ch in string:
        if ch == '(':
            stack.append([ch, 0])
        elif stack[-1][0] == '(':
            _, length = stack.pop()
            stack[-1][1] += length + 2
            longest_len = max(longest_len, stack[-1][1])
        else:
            stack = [['$', 0]]
    return longest_len
