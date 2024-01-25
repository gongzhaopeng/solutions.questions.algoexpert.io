# Algorithmic Beauty Bless You - O(n) time | O(1) space
def waterArea(heights):
    if not heights:
        return 0
    pre_pos1, pre_pos2, step = 0, len(heights) - 1, 1
    if heights[pre_pos1] > heights[pre_pos2]:
        pre_pos1, pre_pos2, step = pre_pos2, pre_pos1, -step
    pos1, pos2 = pre_pos1, pre_pos2
    water_area, cur_pillar_amt = 0, 0
    while pos1 != pos2:
        pos1 += step
        if heights[pos1] > 0:
            if heights[pos1] >= heights[pre_pos1]:
                water_area += heights[pre_pos1] * ((pos1 - pre_pos1) * step - 1) - cur_pillar_amt
                cur_pillar_amt, pre_pos1 = 0, pos1
                if heights[pos1] > heights[pos2]:
                    pos1, pre_pos1, pos2, pre_pos2, step = pos2, pre_pos2, pos1, pre_pos1, -step
            else:
                cur_pillar_amt += heights[pos1]
    return water_area
