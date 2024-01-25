# Algorithmic Beauty Bless You - O(n) time | O(1) space
def hasSingleCycle(array):
    p_cur = array[0] % len(array)
    for _ in range(len(array) - 1):
        if p_cur == 0:
            return False
        p_cur = (p_cur + array[p_cur]) % len(array)
    return p_cur == 0
