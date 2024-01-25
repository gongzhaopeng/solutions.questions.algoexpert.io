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
    reversed_segments = []
    while segments:
        reversed_segments.append(segments.pop())
    return ''.join(reversed_segments)
