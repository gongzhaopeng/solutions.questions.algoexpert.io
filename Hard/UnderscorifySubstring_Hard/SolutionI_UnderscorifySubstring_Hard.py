import itertools
import re


# Algorithmic Beauty Bless You - O(n+m) time | O(n) space
def underscorifySubstring(string, substring):
    spans = [[_.start(1), _.end(1)] for _ in re.finditer(rf'(?=({substring}))', string)]
    if not spans:
        return string
    merged_spans = [[0, 0], spans[0]]
    for span in itertools.islice(spans, 1, len(spans)):
        if span[0] < merged_spans[-1][1] + 1:
            merged_spans[-1][1] = span[1]
        else:
            merged_spans.append(span)
    segments = []
    for i in range(1, len(merged_spans)):
        segments.extend([string[merged_spans[i - 1][1]:merged_spans[i][0]],
                         '_', string[merged_spans[i][0]:merged_spans[i][1]], '_'])
    segments.append(string[spans[-1][1]:])
    return ''.join(segments)
