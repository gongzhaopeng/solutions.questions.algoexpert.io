# Algorithmic Beauty Bless You - O(b+s) time | O(b+s) space
def smallestSubstringContaining(bigString, smallString):
    smallest_span = [0, float('inf')]
    exp_counts = {}
    for ch in smallString:
        exp_counts[ch] = exp_counts.get(ch, 0) + 1
    counts, done_num = {_: 0 for _ in exp_counts}, 0
    begin = stop = 0
    while stop < len(bigString):
        ch = bigString[stop]
        stop += 1
        if ch in counts:
            counts[ch] += 1
            if counts[ch] == exp_counts[ch]:
                done_num += 1
        while begin < stop:
            ch = bigString[begin]
            if ch in counts:
                if counts[ch] <= exp_counts[ch]:
                    break
                counts[ch] -= 1
            begin += 1
        if done_num == len(exp_counts) and stop - begin < smallest_span[1] - smallest_span[0]:
            smallest_span = [begin, stop]
    return '' if smallest_span[1] == float('inf') else bigString[smallest_span[0]:smallest_span[1]]
