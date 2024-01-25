def longestPeak(array):
    inc_count, dec_count, max_peak_size = 0, 0, 0
    for i in range(len(array) - 1):
        delta = array[i + 1] - array[i]
        if delta < 0:
            dec_count += 1
        else:
            if dec_count > 0:
                if inc_count > 0:
                    max_peak_size = max(max_peak_size, inc_count + dec_count)
                    inc_count = 0
                dec_count = 0
            if delta > 0:
                inc_count += 1
            else:
                inc_count = 0
    else:
        if inc_count > 0 and dec_count > 0:
            max_peak_size = max(max_peak_size, inc_count + dec_count)
    return max_peak_size + 1 if max_peak_size > 0 else 0
