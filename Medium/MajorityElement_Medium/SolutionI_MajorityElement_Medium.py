# Algorithmic Beauty Bless You - O(n) time | O(1) space
def majorityElement(array):
    majority, count = None, 0
    for num in array:
        if count == 0:
            majority = num
        count = count + 1 if num == majority else count - 1
    return majority
