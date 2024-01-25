radix_bit_cnt, extractor = 4, 0xF


# Algorithmic Beauty Bless You - O(d*(n+b)) time | O(n+b) space
def radixSort(array):
    max_num, shift_bit_cnt, counts = max(array, default=-1), 0, [0] * (extractor + 1)
    ori_array, dest_array = array, array.copy()
    while max_num > 0:
        counting_sort(ori_array, shift_bit_cnt, counts, dest_array)
        shift_bit_cnt += radix_bit_cnt
        max_num >>= radix_bit_cnt
        ori_array, dest_array = dest_array, ori_array
    if array is not ori_array:
        array[:] = ori_array
    return array


def counting_sort(array, shift_bit_cnt, counts, sorted_array):
    def extract_digit():
        return (num >> shift_bit_cnt) & extractor

    for _ in range(len(counts)):
        counts[_] = 0
    for num in array:
        counts[extract_digit()] += 1
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]
    for num in reversed(array):
        digit = extract_digit()
        counts[digit] -= 1
        sorted_array[counts[digit]] = num
