# Algorithmic Beauty Bless You - O(n) time | O(1) space
def findThreeLargestNumbers(array):
    threes = [float('-inf')] * 3
    for num in array:
        if num > threes[2]:
            threes[0], threes[1], threes[2] = threes[1], threes[2], num
        elif num > threes[1]:
            threes[0], threes[1] = threes[1], num
        elif num > threes[0]:
            threes[0] = num
    return threes
