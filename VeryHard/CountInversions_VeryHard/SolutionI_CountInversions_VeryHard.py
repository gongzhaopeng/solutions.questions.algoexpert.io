# Algorithmic Beauty Bless You - O(nlogn) time | O(n) space
def countInversions(array):
    count, stack, current, aux_array = 0, [], [0, len(array), None, False], array[:]
    while True:
        if current:
            begin, stop, _, flipped = current
            if stop - begin < 2:
                current = None
                continue
            mid = (begin + stop) // 2
            current[2] = mid
            stack.append(current)
            current = [begin, mid, None, not flipped]
        elif stack:
            begin, stop, mid, flipped = stack[-1]
            if mid > 0:
                stack[-1][2] = -mid
                current = [mid, stop, None, not flipped]
                continue
            stack.pop()
            mid = -mid
            p_first, p_second = begin, mid
            src_array, dest_array = (array, aux_array) if flipped else (aux_array, array)
            while True:
                if src_array[p_first] > src_array[p_second]:
                    count += mid - p_first
                    dest_array[begin] = src_array[p_second]
                    p_second += 1
                    if p_second >= stop:
                        while p_first < mid:
                            begin += 1
                            dest_array[begin] = src_array[p_first]
                            p_first += 1
                        break
                else:
                    dest_array[begin] = src_array[p_first]
                    p_first += 1
                    if p_first >= mid:
                        while p_second < stop:
                            begin += 1
                            dest_array[begin] = src_array[p_second]
                            p_second += 1
                        break
                begin += 1
        else:
            break
    return count
