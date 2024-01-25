import operator


# Algorithmic Beauty Bless You - O(nlogn) time | O(n) space
def laptopRentals(times):
    times.sort(key=operator.itemgetter(0))
    sorted_by_end = times.copy()
    sorted_by_end.sort(key=operator.itemgetter(1))
    i, j, used_count = 0, 0, 0
    while i < len(times):
        if sorted_by_end[j][1] <= times[i][0]:
            j += 1
            used_count -= 1
        i += 1
        used_count += 1
    return used_count
