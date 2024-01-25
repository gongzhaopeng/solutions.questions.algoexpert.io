# Algorithmic Beauty Bless You - O(n) time | O(1) space
def missingNumbers(nums):
    count, p_cur = len(nums), 0
    nums.extend([None] * 2)
    for _ in range(count):
        ne = next(i for i in range(p_cur, len(nums)) if nums[i])
        due_pos = nums[ne] - 1
        if ne == due_pos:
            nums[ne], p_cur = 0, ne + 1
        else:
            nums[ne], nums[due_pos] = nums[due_pos], 0
    return [i + 1 for i in range(len(nums)) if nums[i] is None]
