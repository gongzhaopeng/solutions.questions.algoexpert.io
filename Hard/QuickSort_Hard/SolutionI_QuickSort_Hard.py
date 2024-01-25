import random


# Algorithmic Beauty Bless You - O(nlog(n)) time | O(log(n)) space
def quickSort(array):
    stack = [(0, len(array) - 1)]
    while stack:
        p_left, p_right = popped = stack.pop()
        if p_right - p_left < 1:
            continue
        p_ref = random.randint(p_left, p_right)
        ref, array[p_ref] = array[p_ref], array[p_right]
        p_blank, p_right, finding_bigger = p_right, p_right - 1, True
        while p_left <= p_right:
            if finding_bigger:
                if array[p_left] > ref:
                    array[p_blank], p_blank, finding_bigger = array[p_left], p_left, False
                p_left += 1
            else:
                if array[p_right] < ref:
                    array[p_blank], p_blank, finding_bigger = array[p_right], p_right, True
                p_right -= 1
        array[p_blank] = ref
        stack.extend([(popped[0], p_blank - 1), (p_blank + 1, popped[1])])
    return array
