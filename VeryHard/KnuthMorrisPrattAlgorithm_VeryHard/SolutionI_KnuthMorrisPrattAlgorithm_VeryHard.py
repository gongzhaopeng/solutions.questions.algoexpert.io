# Algorithmic Beauty Bless You - O(n + m) time | O(m) space
def knuthMorrisPrattAlgorithm(string, substring):
    matches = []
    pattern_table = create_pattern_table(substring)
    j = 0
    for i, char in enumerate(string):
        if char == substring[j]:
            j += 1
            if j != len(substring):
                continue
            # return True
            matches.append(i)
        elif j == 0:
            continue
        j = determine_longest_sub_prefix(substring, j - 1, char, pattern_table) + 1
    return len(matches) > 0


def create_pattern_table(substring):
    pattern_table = [-1] * len(substring)
    for i in range(1, len(substring)):
        pattern_table[i] = determine_longest_sub_prefix(substring, i - 1, substring[i], pattern_table)
    return pattern_table


def determine_longest_sub_prefix(substring, pre_pos, cur_char, pattern_table):
    j = pattern_table[pre_pos] + 1
    while True:
        if cur_char == substring[j]:
            return j
        elif j == 0:
            return -1
        j = pattern_table[j - 1] + 1
