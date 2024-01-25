from bisect import bisect_left, bisect_right


# Algorithmic Beauty Bless You - O(nlogn) time | O(1) space
def sweetAndSavory(dishes, target):
    paring, min_diff = [0, 0], float('inf')
    dishes.sort()
    sweet_pos = bisect_left(dishes, 0) - 1
    savory_pos = sweet_pos + 1
    while sweet_pos >= 0 and savory_pos < len(dishes):
        sweet, savory = dishes[sweet_pos], dishes[savory_pos]
        diff = target - (sweet + savory)
        if diff < 0:
            sweet_pos -= 1
        elif diff > 0:
            if diff < min_diff:
                paring, min_diff = [sweet, savory], diff
            savory_pos += 1
        else:
            paring = [sweet, savory]
            break
    return paring
