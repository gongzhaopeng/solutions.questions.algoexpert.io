# Algorithmic Beauty Bless You - O(n) time | O(n) space
def maximizeExpression(array):
    if len(array) < 4:
        return 0
    pre_results = [0] * len(array)
    cur_results, is_add = pre_results.copy(), True
    for start in range(4):
        cur_results[start - 1] = float('-inf')
        for i in range(start, len(array)):
            if is_add:
                result = pre_results[i - 1] + array[i]
            else:
                result = pre_results[i - 1] - array[i]
            cur_results[i] = max(result, cur_results[i - 1])
        pre_results, cur_results, is_add = cur_results, pre_results, not is_add
    return pre_results[-1]
