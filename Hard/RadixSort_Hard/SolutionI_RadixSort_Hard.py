# Algorithmic Beauty Bless You - O(d*(n+b)) time | O(n+b) space
def radixSort(array):
    radix_bit_cnt, extractor, shift_bit_cnt = 4, 0xF, 0
    buckets = [[] for _ in range(extractor + 1)]
    while len(buckets[0]) != len(array):
        for bucket in buckets:
            bucket.clear()
        for num in array:
            b = (num >> shift_bit_cnt) & extractor
            buckets[b].append(num)
        count = 0
        for bucket in buckets:
            array[count:count + len(bucket)] = bucket
            count += len(bucket)
        shift_bit_cnt += radix_bit_cnt
    return array
