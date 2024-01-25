import math


# Algorithmic Beauty Bless You - O(n^2+m) time | O(n) space
def patternMatcher(pattern, string):
    str_len = len(string)
    x_count = pattern.count('x')
    y_count = len(pattern) - x_count
    if x_count == 0:
        if str_len % y_count == 0:
            len_pairs = [(0, str_len // y_count)]
        else:
            return []
    elif y_count == 0:
        if str_len % x_count == 0:
            len_pairs = [(str_len // x_count, 0)]
        else:
            return []
    else:
        len_pairs = ((sx_len, str_len - sx_len * x_count) for sx_len in range(1, math.ceil(str_len / x_count)))
        len_pairs = map(lambda _: (_[0], _[1] // y_count), filter(lambda _: _[1] % y_count == 0, len_pairs))
    for sx_len, sy_len in len_pairs:
        p_sx = p_sy = None
        p_cur = 0
        for pch in pattern:
            if pch == 'x':
                if p_sx is None:
                    p_sx = p_cur
                elif not is_matched(string, p_cur, p_sx, sx_len):
                    break
                p_cur += sx_len
            else:
                if p_sy is None:
                    p_sy = p_cur
                elif not is_matched(string, p_cur, p_sy, sy_len):
                    break
                p_cur += sy_len
        else:
            return ['' if p_sx is None else string[p_sx:p_sx + sx_len],
                    '' if p_sy is None else string[p_sy:p_sy + sy_len]]
    return []


def is_matched(string, p1, p2, length):
    return all(string[p1 + offset] == string[p2 + offset] for offset in range(length))
