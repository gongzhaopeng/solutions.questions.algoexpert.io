# Algorithmic Beauty Bless You - O(log(min(m,n))) time | O(1) space
def medianOfTwoSortedArrays(arrayOne, arrayTwo):
    if len(arrayOne) > len(arrayTwo):
        arrayOne, arrayTwo = arrayTwo, arrayOne
    p_left, p_right = 0, len(arrayOne) - 1
    p_left_median = (len(arrayOne) + len(arrayTwo) - 1) // 2
    while True:
        p_cut_one = (p_left + p_right) // 2
        p_cut_two = p_left_median - p_cut_one - 1
        p_greater_one, p_greater_two = p_cut_one + 1, p_cut_two + 1
        less_one = float('-inf') if p_cut_one < 0 else arrayOne[p_cut_one]
        greater_one = arrayOne[p_greater_one] if p_greater_one < len(arrayOne) else float('inf')
        less_two = float('-inf') if p_cut_two < 0 else arrayTwo[p_cut_two]
        greater_two = arrayTwo[p_greater_two] if p_greater_two < len(arrayTwo) else float('inf')
        if less_one > greater_two:
            p_right = p_cut_one - 1
        elif less_two > greater_one:
            p_left = p_cut_one + 1
        elif (len(arrayOne) + len(arrayTwo)) % 2:
            return max(less_one, less_two)
        else:
            return (max(less_one, less_two) + min(greater_one, greater_two)) / 2
