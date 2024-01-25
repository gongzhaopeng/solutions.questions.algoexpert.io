# Algorithmic Beauty Bless You - O(n) time | O(n) space
def reverseWordsInString(string):
    segments, start, whitespace = [], 0, ' '
    for stop in range(1, len(string)):
        if string[start] == whitespace:
            if string[stop] == whitespace:
                continue
        elif string[stop] != whitespace:
            continue
        segments.append(string[start:stop])
        start = stop
    segments.append(string[start:])
    reverse_list(segments)
    return ''.join(segments)


def reverse_list(li):
    left, right = 0, len(li) - 1
    while left < right:
        li[left], li[right] = li[right], li[left]
        left, right = left + 1, right - 1
