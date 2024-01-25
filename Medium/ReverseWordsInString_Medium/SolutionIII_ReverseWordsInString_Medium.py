# Algorithmic Beauty Bless You - O(n) time | O(n) space
def reverseWordsInString(string):
    rev, stop, end, whitespace = [], len(string) - 1, len(string) - 1, ' '
    while stop > 0:
        stop -= 1
        if string[end] == whitespace:
            if string[stop] == whitespace:
                continue
        elif string[stop] != whitespace:
            continue
        rev.append(string[stop + 1: end + 1])
        end = stop
    rev.append(string[:end + 1])
    return ''.join(rev)
