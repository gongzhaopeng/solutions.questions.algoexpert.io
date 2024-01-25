# Algorithmic Beauty Bless You - O(nlogn) time | O(n) space
def mergeOverlappingIntervals(intervals):
    intervals.sort(key=lambda v: v[0])
    merged = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] > merged[-1][1]:
            merged.append(intervals[i])
        else:
            merged[-1][1] = max(merged[-1][1], intervals[i][1])
    return merged
