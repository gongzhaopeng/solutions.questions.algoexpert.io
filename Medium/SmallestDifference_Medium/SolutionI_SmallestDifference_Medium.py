def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    chosen_pair = [arrayOne[0], arrayTwo[0]]
    smallest_diff = chosen_pair[0] - chosen_pair[1]
    one_is_bigger = True
    array_big = arrayOne
    array_small = arrayTwo
    if smallest_diff < 0:
        one_is_bigger = False
        smallest_diff = -smallest_diff
        array_big = arrayTwo
        array_small = arrayOne
    index_big = 0
    index_small = 0
    while True:
        elem_big = array_big[index_big]
        index_small = find_less_closest_index(array_small, index_small, elem_big)
        elem_small = array_small[index_small]
        diff = elem_big - elem_small
        if diff < smallest_diff:
            chosen_pair = [elem_big, elem_small] if one_is_bigger else [elem_small, elem_big]
            smallest_diff = diff
        index_small += 1
        if index_small >= len(array_small):
            break
        if smallest_diff == 0:
            break
        one_is_bigger = not one_is_bigger
        temp = array_small
        array_small = array_big
        array_big = temp
        temp = index_small
        index_small = index_big
        index_big = temp
    return chosen_pair


def find_less_closest_index(array, start_pos, target):
    start_pos += 1
    while start_pos < len(array):
        if array[start_pos] > target:
            break
        start_pos += 1
    return start_pos - 1
