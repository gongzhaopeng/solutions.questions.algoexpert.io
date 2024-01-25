from itertools import chain


# Algorithmic Beauty Bless You - O(h*w) time | O(w) space
def largestPark(land):
    max_area, bars = 0, [0] * (len(land[0]) + 1)
    for row in land:
        stack = [-1]
        for i, occupied in enumerate(chain(row, [True])):
            bars[i] = 0 if occupied else bars[i] + 1
            while True:
                h_park = bars[stack[-1]]
                if h_park > bars[i]:
                    stack.pop()
                    max_area = max(max_area, (i - stack[-1] - 1) * h_park)
                    continue
                if h_park < bars[i]:
                    stack.append(i)
                else:
                    stack[-1] = i
                break
    return max_area
