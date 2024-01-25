# Algorithmic Beauty Bless You - O(n^2) time | O(n) space
def countSquares(points):
    count = 0
    registry = {(x, y) for (x, y) in points}
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        for j in range(i + 1, len(points)):
            x2, y2 = points[j]
            if x1 == x2 and y1 == y2:
                continue
            mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
            delta_x, delta_y = mid_y - y1, x1 - mid_x
            x3, y3 = mid_x + delta_x, mid_y + delta_y
            x4, y4 = mid_x - delta_x, mid_y - delta_y
            if (x3, y3) in registry and (x4, y4) in registry:
                count += 1
    return count / 2
