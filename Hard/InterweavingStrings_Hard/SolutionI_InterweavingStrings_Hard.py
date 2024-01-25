# Algorithmic Beauty Bless You - O(m*n) time | O(n) space
def interweavingStrings(one, two, three):
    if len(one) + len(two) != len(three):
        return False
    pre_dpt = [False] * (len(two) + 1)
    cur_dpt = pre_dpt.copy()
    pre_dpt[-1] = True
    for j in range(len(two)):
        if two[j] != three[j]:
            break
        pre_dpt[j] = True
    for i in range(len(one)):
        any_match = cur_dpt[-1] = pre_dpt[-1] and one[i] == three[i]
        for j in range(len(two)):
            p3 = i + j + 1
            cur_dpt[j] = two[j] == three[p3] and cur_dpt[j - 1] or one[i] == three[p3] and pre_dpt[j]
            any_match = any_match or cur_dpt[j]
        if not any_match:
            return False
        pre_dpt, cur_dpt = cur_dpt, pre_dpt
    return pre_dpt[len(two) - 1]
