# Algorithmic Beauty Bless You - O(n) time | O(1) space
def kadanesAlgorithm(array):
    max_sum, cur_sum = float('-inf'), 0
    for num in array:
        cur_sum += num
        max_sum, cur_sum = max(max_sum, cur_sum), max(0, cur_sum)
    return max_sum
