def largestRange(array):
    nums = {n: True for n in array}
    max_range_head = None
    max_range_len = 0
    for num in nums:
        if not nums.setdefault(num, False):
            continue
        pre_head = num - 1
        while pre_head in nums:
            nums[pre_head] = False
            pre_head -= 1
        post_tail = num + 1
        while post_tail in nums:
            nums[post_tail] = False
            post_tail += 1
        cur_range_len = post_tail - pre_head - 1
        if cur_range_len > max_range_len:
            max_range_len = cur_range_len
            max_range_head = pre_head + 1
    return [max_range_head, max_range_head + max_range_len - 1]
