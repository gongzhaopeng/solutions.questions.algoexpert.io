# Algorithmic Beauty Bless You - O(n) time | O(1) space
def missingNumbers(nums):
    extras, missed = [1] * 2, []
    for e in nums:
        pos = abs(e) - 1
        if pos < len(nums):
            nums[pos] = -nums[pos]
        else:
            extras[pos - len(nums)] = -1
    for i, e in enumerate(nums):
        if nums[i] > 0:
            missed.append(i + 1)
        else:
            nums[i] = -nums[i]
    for i, e in enumerate(extras):
        if extras[i] > 0:
            missed.append(len(nums) + 1 + i)
    return missed
