def largestRange(array):
    head_refs = {}
    tail_refs = {}
    for e in array:
        head_range = head_refs.pop(e, None)
        tail_range = tail_refs.pop(e, None)
        if head_range:
            if tail_range:
                head = e - tail_range[0] - 1
                new_range = head_refs[head]
                new_range[0] = head_range[0] + tail_range[0] + 1
                tail = e + head_range[0] + 1
                tail_refs[tail] = new_range
            else:
                new_head = e - 1
                head_range[0] += 1
                ret_range = head_refs.setdefault(new_head, head_range)
                if head_range is not ret_range:
                    tail = new_head + head_range[0] + 1
                    del tail_refs[tail]
        elif tail_range:
            new_tail = e + 1
            tail_range[0] += 1
            ret_range = tail_refs.setdefault(new_tail, tail_range)
            if tail_range is not ret_range:
                head = new_tail - tail_range[0] - 1
                del head_refs[head]
        else:
            new_head = e - 1
            new_tail = e + 1
            if new_head not in head_refs and new_tail not in tail_refs:
                new_range = [1]
                head_refs[new_head] = new_range
                tail_refs[new_tail] = new_range
    optimal_head = None
    max_len = 0
    for (head, r) in head_refs.items():
        if r[0] > max_len:
            optimal_head = head
            max_len = r[0]
    return [optimal_head + 1, optimal_head + max_len]
