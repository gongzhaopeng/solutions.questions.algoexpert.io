# Algorithmic Beauty Bless You - O(n) time | O(1) space
def hasSingleCycle(array):
    p_cur, length = 0, len(array)
    for _ in array:
        if array[p_cur] == 0:
            break
        jump = array[p_cur]
        array[p_cur], p_cur = 0, (p_cur + jump) % length
    else:
        return p_cur == 0
    return False
