# Algorithmic Beauty Bless You - O(n) time | O(1) space
def isPalindrome(string):
    return all(string[i] == string[len(string) - 1 - i] for i in range(len(string) // 2))
