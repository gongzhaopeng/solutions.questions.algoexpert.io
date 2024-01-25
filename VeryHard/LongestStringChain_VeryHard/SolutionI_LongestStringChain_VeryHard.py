# Algorithmic Beauty Bless You - O(n*m^2+nlogn) time | O(nm) space
def longestStringChain(strings):
    longest_chain = []
    strings.sort(key=len)
    str_registry = {s: i for i, s in enumerate(strings)}
    chains = [[None, 0]] * len(strings)
    longest_len, p_longest_chain = 0, None
    for p_cur, s in enumerate(strings):
        for i in range(len(s)):
            candi = s[:i] + s[i + 1:]
            p_candi = str_registry.get(candi, -1)
            if p_candi < 0:
                continue
            cur_len = chains[p_candi][1] + 1
            if cur_len > chains[p_cur][1]:
                chains[p_cur] = [p_candi, cur_len]
            if cur_len > longest_len:
                longest_len, p_longest_chain = cur_len, p_cur
    while p_longest_chain is not None:
        longest_chain.append(strings[p_longest_chain])
        p_longest_chain = chains[p_longest_chain][0]
    return longest_chain
