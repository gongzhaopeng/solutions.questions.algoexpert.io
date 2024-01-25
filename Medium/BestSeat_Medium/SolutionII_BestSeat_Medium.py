# Algorithmic Beauty Bless You - O(n) time | O(1) space
def bestSeat(seats):
    best_start, max_space = -1, 0
    free_start = None
    for i in range(len(seats)):
        if seats[i] == 0:
            if not free_start:
                free_start = i
        elif free_start:
            space = i - free_start
            if space > max_space:
                best_start, max_space = free_start, space
            free_start = None
    return best_start + int((max_space - 1) / 2)
