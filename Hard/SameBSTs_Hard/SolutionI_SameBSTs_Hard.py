# Algorithmic Beauty Bless You - O(n^2) time | O(d) space
def sameBsts(arrayOne, arrayTwo):
    stack = []
    current = 0, 0, float('-inf'), float('inf')
    while True:
        index_1, index_2, minimum, maximum = current
        if index_1 < 0 <= index_2 or index_1 >= 0 > index_2:
            return False
        if index_1 >= 0:
            if arrayOne[index_1] != arrayTwo[index_2]:
                return False
            stack.append((index_1, index_2, minimum, maximum))
            cur_v = arrayOne[index_1]
            index_1 = first_lt(arrayOne, index_1, minimum)
            index_2 = first_lt(arrayTwo, index_2, minimum)
            current = index_1, index_2, minimum, cur_v
        elif stack:
            index_1, index_2, minimum, maximum = stack.pop()
            cur_v = arrayOne[index_1]
            index_1 = first_gte(arrayOne, index_1, maximum)
            index_2 = first_gte(arrayTwo, index_2, maximum)
            current = index_1, index_2, cur_v, maximum
        else:
            return True


def first_lt(array, p_ref, minimum):
    return first_match(array, p_ref, lambda v: minimum <= v < array[p_ref])


def first_gte(array, p_ref, maximum):
    return first_match(array, p_ref, lambda v: array[p_ref] <= v < maximum)


def first_match(array, p_ref, condition):
    return next((i for i in range(p_ref + 1, len(array)) if condition(array[i])), -1)
