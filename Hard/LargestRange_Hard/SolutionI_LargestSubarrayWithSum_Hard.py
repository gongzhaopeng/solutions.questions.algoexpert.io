def longestSubarrayWithSum(array, targetSum):
    if not array:
        return []
    sub_indices = [0, -1]
    p_head, p_tail, cur_sum = 0, 0, array[0]
    while True:
        if cur_sum > targetSum:
            cur_sum -= array[p_head]
            p_head += 1
        else:
            if cur_sum == targetSum and p_tail - p_head > sub_indices[1] - sub_indices[0]:
                sub_indices[0], sub_indices[1] = p_head, p_tail
            p_tail += 1
            if p_tail >= len(array):
                break
            cur_sum += array[p_tail]
    return sub_indices if sub_indices[1] > -1 else []
