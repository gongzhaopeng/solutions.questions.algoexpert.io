# Algorithmic Beauty Bless You - O(n) time | O(n) space
def longestBalancedSubstring(string):
    longest_len, stack = 0, [-1]
    for i in range(len(string)):
        if string[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                longest_len = max(longest_len, i - stack[-1])
    return longest_len
