# Algorithmic Beauty Bless You - O(nlogn) time | O(n) space
def mergeSort(array):
    stack, current, aux_array = [], [0, len(array) - 1, None, False], array[:]  # current=[left, right, mid, flipped]
    while True:
        if current:
            left, right, _, flipped = current
            if left == right:
                current = None
                continue
            mid = (left + right) // 2
            current[2] = mid
            stack.append(current)
            current = [left, mid, None, not flipped]
        elif stack:
            left, right, mid, flipped = stack[-1]
            if mid > 0:
                stack[-1][2] = -mid
                current = [mid + 1, right, None, not flipped]
                continue
            stack.pop()
            mid = -mid
            p_first, p_second = left, mid + 1
            src_array, dest_array = (array, aux_array) if flipped else (aux_array, array)
            while True:
                if src_array[p_first] > src_array[p_second]:
                    dest_array[left] = src_array[p_second]
                    p_second += 1
                    if p_second > right:
                        while p_first <= mid:
                            left += 1
                            dest_array[left] = src_array[p_first]
                            p_first += 1
                        break
                else:
                    dest_array[left] = src_array[p_first]
                    p_first += 1
                    if p_first > mid:
                        while p_second <= right:
                            left += 1
                            dest_array[left] = src_array[p_second]
                            p_second += 1
                        break
                left += 1
        else:
            break
    return array
