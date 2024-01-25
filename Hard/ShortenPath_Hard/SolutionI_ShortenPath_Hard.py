# Algorithmic Beauty Bless You - O(n) time | O(n) space
def shortenPath(path):
    stack = []
    seg_start = 0
    while seg_start < len(path):
        seg_end = next_segment(path, seg_start)
        segment, seg_start = path[seg_start:seg_end], seg_end + 1
        if segment == '':
            if not stack:
                stack.append(segment)
        elif segment == '.':
            continue
        elif segment == '..':
            if not stack or stack[-1] == '..':
                stack.append(segment)
            elif stack[-1] != '':
                stack.pop()
        else:
            stack.append(segment)
    if len(stack) == 1 and stack[0] == '':
        return '/'
    return '/'.join(stack)


def next_segment(path, start):
    while start < len(path):
        if path[start] == '/':
            return start
        start += 1
    return start
