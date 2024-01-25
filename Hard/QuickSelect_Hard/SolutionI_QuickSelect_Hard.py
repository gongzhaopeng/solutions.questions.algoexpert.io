import random


# Algorithmic Beauty Bless You - O(n) time | O(1) space
def quickselect(array, k):
    p_head, p_tail = 0, len(array) - 1
    while True:
        p_pivot = random.randint(p_head, p_tail)
        pivot, array[p_pivot], p_blank, finding_bigger = array[p_pivot], array[p_tail], p_tail, True
        p_left, p_right = p_head, p_tail - 1
        while p_left <= p_right:
            if finding_bigger:
                if array[p_left] > pivot:
                    array[p_blank], p_blank, finding_bigger = array[p_left], p_left, False
                p_left += 1
            else:
                if array[p_right] < pivot:
                    array[p_blank], p_blank, finding_bigger = array[p_right], p_right, True
                p_right -= 1
        array[p_blank] = pivot
        if p_blank < k - 1:
            p_head = p_blank + 1
        elif p_blank > k - 1:
            p_tail = p_blank - 1
        else:
            return pivot
