def lineThroughPoints(points):
    max_linear_count, counts_in_slope = 1, {}
    for i in range(len(points) - 1):
        counts_in_slope.clear()
        for j in range(i + 1, len(points)):
            slope = calc_slope(points[i], points[j])
            wrapped_count = counts_in_slope.setdefault(slope, [1])
            wrapped_count[0] += 1
        max_linear_count = max(max_linear_count,
                               max(map(lambda c: c[0], counts_in_slope.values())))
    return max_linear_count


def calc_slope(p1, p2):
    def calc_gcd(a, b):
        if a < b:
            b, a = a, b
        while b != 0:
            a, b = b, a % b
        return abs(a)

    if p1[0] > p2[0]:
        p1, p2 = p2, p1
    x_diff, y_diff = p2[0] - p1[0], p2[1] - p1[1]
    gcd = calc_gcd(x_diff, y_diff)
    return x_diff // gcd, y_diff // gcd
