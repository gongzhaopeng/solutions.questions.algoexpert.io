# Algorithmic Beauty Bless You - O(n) time | O(1) space
def maximizeExpression(array):
    if len(array) < 4:
        return 0
    max_1_tuple = array[0]
    max_2_tuple = max_1_tuple - array[1]
    max_3_tuple = max_2_tuple + array[2]
    max_4_tuple = max_3_tuple - array[3]
    for i in range(1, len(array) - 3):
        max_1_tuple = max(max_1_tuple, array[i])
        max_2_tuple = max(max_2_tuple, max_1_tuple - array[i + 1])
        max_3_tuple = max(max_3_tuple, max_2_tuple + array[i + 2])
        max_4_tuple = max(max_4_tuple, max_3_tuple - array[i + 3])
    return max_4_tuple
