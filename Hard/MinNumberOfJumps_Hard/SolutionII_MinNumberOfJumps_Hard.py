# Algorithmic Beauty Bless You - O(n) time | O(1) space
def minNumberOfJumps(array):
    jump, jump_span = 0, [0, 1]
    while jump_span[1] < len(array):
        jump, new_span = jump + 1, [jump_span[1], jump_span[1] + 1]
        for i in range(*jump_span):
            new_span[1] = max(new_span[1], i + array[i] + 1)
        jump_span = new_span
    return jump
