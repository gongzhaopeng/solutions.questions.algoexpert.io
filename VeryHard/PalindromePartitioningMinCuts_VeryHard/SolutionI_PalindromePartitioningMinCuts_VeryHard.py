# Algorithmic Beauty Bless You - O(n^2) time | O(n) space
def palindromePartitioningMinCuts(string):
    min_cuts_registry = [0] * len(string)
    tail_pals_indicator = min_cuts_registry.copy()
    tail_pals_indicator[0] = True
    for i in range(1, len(string)):
        min_cuts_registry[i] = min_cuts_registry[i - 1] + 1
        tail_pals_indicator[i] = True
        for j in range(0, i):
            tail_pals_indicator[j] = tail_pals_indicator[j + 1] and string[j] == string[i]
        if tail_pals_indicator[0]:
            min_cuts_registry[i] = 0
        else:
            for j in range(1, i):
                if tail_pals_indicator[j]:
                    local_min_cuts = min_cuts_registry[j - 1] + 1
                    min_cuts_registry[i] = min(min_cuts_registry[i], local_min_cuts)
    return min_cuts_registry[-1]
