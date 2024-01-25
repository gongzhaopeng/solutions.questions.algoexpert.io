from itertools import chain


# Algorithmic Beauty Bless You - O(h*w) time | O(w) space
def largestPark(land):
    max_area, bars, stack = 0, [0] * (len(land[0]) + 1), [(0, -1)]
    for row in land:
        for i, occupied in enumerate(chain(row, [True])):
            bars[i], p_left = 0 if occupied else bars[i] + 1, i
            while True:
                h_park, j = stack[-1]
                if h_park > bars[i]:
                    max_area, p_left = max(max_area, (i - j) * h_park), j
                    stack.pop()
                    continue
                if h_park < bars[i]:
                    stack.append((bars[i], p_left))
                break
    return max_area
