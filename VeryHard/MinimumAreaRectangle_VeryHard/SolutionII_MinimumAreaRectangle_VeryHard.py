# O(max(NumOfVerticalEdges, n*log(n))) time  | O(NumOfVerticalEdges) space
def minimumAreaRectangle(points):
    min_area = float('inf')
    points_by_cols = {}
    for p in points:
        points_at_col = points_by_cols.setdefault(p[0], [])
        points_at_col.append(p[1])
    rightest_y_dir_edges = {}
    for x2 in sorted(points_by_cols.keys()):
        ys_at_col_x2 = points_by_cols[x2]
        ys_at_col_x2.sort()
        for i2, y2 in enumerate(ys_at_col_x2):
            for i1 in range(i2):
                y1 = ys_at_col_x2[i1]
                wrapped_x1 = rightest_y_dir_edges.setdefault((y1, y2), [x2])
                cur_area = (x2 - wrapped_x1[0]) * (y2 - y1)
                wrapped_x1[0] = x2
                if cur_area and cur_area < min_area:
                    min_area = cur_area
    return 0 if min_area == float('inf') else min_area
