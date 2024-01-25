# Algorithmic Beauty Bless You - O(n) time | O(n) space
def largestRectangleUnderSkyline(buildings):
    largest, stack = 0, [(-1, 0)]
    buildings.append(0)
    for pos, height in enumerate(buildings):
        while True:
            pre_height = stack[-1][1]
            if pre_height < height:
                break
            stack.pop()
            if pre_height == height:
                break
            largest = max(largest, pre_height * (pos - stack[-1][0] - 1))
        stack.append((pos, height))
    return largest
