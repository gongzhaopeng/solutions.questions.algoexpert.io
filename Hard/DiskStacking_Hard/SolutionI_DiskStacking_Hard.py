import operator


# Algorithmic Beauty Bless You - O(n^2) time | O(n) space
def diskStacking(disks):
    disks.sort(key=operator.itemgetter(0), reverse=True)
    opt_heights, sequences, p_optimal_tail = [0] * len(disks), [-1] * len(disks), 0
    for i in range(len(disks)):
        for j in range(0, i):
            if all(map(lambda _: disks[i][_] < disks[j][_], range(3))) and opt_heights[j] > opt_heights[i]:
                opt_heights[i], sequences[i] = opt_heights[j], j
        opt_heights[i] += disks[i][-1]
        if opt_heights[i] > opt_heights[p_optimal_tail]:
            p_optimal_tail = i
    stacking = []
    while p_optimal_tail != -1:
        stacking.append(disks[p_optimal_tail])
        p_optimal_tail = sequences[p_optimal_tail]
    return stacking
