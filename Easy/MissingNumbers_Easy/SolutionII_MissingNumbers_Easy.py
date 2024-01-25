import itertools


# Algorithmic Beauty Bless You - O(n) time | O(1) space
def missingNumbers(nums):
    extras = [1] * 2
    for e in nums:
        pos = abs(e) - 1
        if pos < len(nums):
            nums[pos] = -nums[pos]
        else:
            extras[pos - len(nums)] = -1
    return [i + 1 for i, e in enumerate(itertools.chain(nums, extras)) if e > 0]
