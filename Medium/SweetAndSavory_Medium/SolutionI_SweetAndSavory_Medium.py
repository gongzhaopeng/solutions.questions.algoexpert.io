from bisect import bisect_left, bisect_right


# Algorithmic Beauty Bless You - O(nlogn) time | O(1) space
def sweetAndSavory(dishes, target):
    paring, min_diff = [0, 0], float('inf')
    dishes.sort()
    sweet_up_bound = min(target, 0)
    sweet_pos = bisect_right(dishes, sweet_up_bound) - 1
    savory_pos_bottom = bisect_right(dishes, 0, lo=sweet_pos + 1)
    while sweet_pos >= 0 and savory_pos_bottom < len(dishes):
        sweet = dishes[sweet_pos]
        savory_up_bound = target - sweet + 1
        savory_pos = bisect_left(dishes, savory_up_bound, lo=savory_pos_bottom) - 1
        if savory_pos_bottom <= savory_pos:
            savory = dishes[savory_pos]
            diff = target - (sweet + savory)
            if diff < min_diff:
                paring, min_diff = [sweet, savory], diff
            savory_pos_bottom = savory_pos + 1
        sweet_pos = bisect_left(dishes, sweet, hi=sweet_pos) - 1
    return paring
