# Algorithmic Beauty Bless You - O(n) time | O(n) space
def zeroSumSubarray(nums):
    cur_sum, pre_sums = 0, {0}
    for e in nums:
        cur_sum += e
        if cur_sum in pre_sums:
            return True
        pre_sums.add(cur_sum)
    return False
