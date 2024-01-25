# Algorithmic Beauty Bless You - O(n) time | O(1) space
def waterArea(heights):
    if not heights:
        return 0
    water_area, p_left, p_right = 0, 0, len(heights) - 1
    low_left, low_right = heights[p_left], heights[p_right]
    while p_left != p_right:
        if heights[p_left] < heights[p_right]:
            p_left += 1
            low_left = max(low_left, heights[p_left])
            water_area += low_left - heights[p_left]
        else:
            p_right -= 1
            low_right = max(low_right, heights[p_right])
            water_area += low_right - heights[p_right]
    return water_area
