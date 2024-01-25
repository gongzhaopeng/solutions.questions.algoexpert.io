# Algorithmic Beauty Bless You - O(n*n!) time | O(n*n!) space
def getPermutations(array):
    permutations, stack, p_cur = [], [], 0 if array else None
    while True:
        if p_cur is not None:
            stack.append(p_cur)
            p_cur = len(stack)
            if p_cur == len(array):
                p_cur = None
                permutations.append(array[:])
        elif stack:
            swap(array, len(stack) - 1, stack[-1])
            stack[-1] += 1
            if stack[-1] < len(array):
                swap(array, len(stack) - 1, stack[-1])
                p_cur = len(stack)
            else:
                stack.pop()
        else:
            break
    return permutations


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
