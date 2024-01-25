def minimumAreaRectangle(points):
    min_area = float('inf')
    point_set = {(p[0], p[1]) for p in points}
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            p1, p2 = (points[i], points[j]) if points[i][0] < points[j][0] else (points[j], points[i])
            if p1[0] == p2[0] or p1[1] >= p2[1]:
                continue
            if (p1[0], p2[1]) not in point_set or (p2[0], p1[1]) not in point_set:
                continue
            cur_area = (p2[0] - p1[0]) * (p2[1] - p1[1])
            if cur_area < min_area:
                min_area = cur_area
    return 0 if min_area == float('inf') else min_area
