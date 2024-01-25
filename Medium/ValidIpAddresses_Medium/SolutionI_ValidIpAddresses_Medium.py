# Algorithmic Beauty Bless You - O(1) time | O(1) space
def validIPAddresses(string):
    addresses, dpt, stack, current = [], {}, [], [3, len(string), None, None]
    while True:
        if current:
            rank, stop, *_ = current
            if (rank, stop) in dpt:
                current = None
                continue
            dpt[(rank, stop)] = []
            if rank == 0:
                if is_valid_seg(0, stop, string):
                    dpt[(rank, stop)].append([])
                current = None
                continue
            start, max_start = max(stop - 3, rank), min(stop - 1, 3 * rank)
            start = next_valid_seg(start, max_start, stop, string)
            if start < 0:
                current = None
                continue
            current[-2], current[-1] = start, max_start
            stack.append(current)
            current = [rank - 1, start, None, None]
        elif stack:
            rank, stop, start, max_start = stack[-1]
            dpt[(rank, stop)].extend([*_, start] for _ in dpt[(rank - 1, start)])
            next_start = next_valid_seg(start + 1, max_start, stop, string)
            if next_start < 0:
                stack.pop()
            else:
                stack[-1][-2] = next_start
                current = [rank - 1, next_start, None, None]
        else:
            break
    for cut in dpt[(3, len(string))]:
        addresses.append('.'.join([string[:cut[0]],
                                   *(string[cut[_ - 1]:cut[_]] for _ in range(1, len(cut))),
                                   string[cut[-1]:len(string)]]))
    return addresses


def next_valid_seg(min_start, max_start, stop, string):
    for start in range(min_start, max_start + 1):
        if is_valid_seg(start, stop, string):
            return start
    return -1


def is_valid_seg(start, stop, string):
    if stop - start > 1 and string[start] == '0':
        return False
    return int(string[start:stop]) < 256
