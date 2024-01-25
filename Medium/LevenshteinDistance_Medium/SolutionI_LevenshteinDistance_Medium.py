# Algorithmic Beauty Bless You - O(nm) time | O(min(n,m)) space
def levenshteinDistance(str1, str2):
    if len(str1) < len(str2):
        str1, str2 = str2, str1
    if not str2:
        return len(str1)
    pre_dpt = list(range(1, len(str2) + 1))
    pre_dpt.append(0)
    cur_dpt = pre_dpt.copy()
    for i, ch1 in enumerate(str1):
        cur_dpt[-1] = i + 1
        for j, ch2 in enumerate(str2):
            cur_dpt[j] = pre_dpt[j - 1] if ch1 == ch2 else min(pre_dpt[j - 1], pre_dpt[j], cur_dpt[j - 1]) + 1
        pre_dpt, cur_dpt = cur_dpt, pre_dpt
    return pre_dpt[-2]
