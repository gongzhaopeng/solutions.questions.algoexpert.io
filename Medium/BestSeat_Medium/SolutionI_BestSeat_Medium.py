import math


# Algorithmic Beauty Bless You - O(n) time | O(1) space
def bestSeat(seats):
    pre_best, max_space = -1, 0
    pre_free = 0
    while pre_free < len(seats):
        post_free = next((i for i in range(pre_free + 1, len(seats)) if seats[i] == 1), pre_free + 1)
        space = post_free - pre_free - 1
        if space > max_space:
            pre_best, max_space = pre_free, space
        pre_free = post_free
    return pre_best + math.ceil(max_space / 2)
