# Algorithmic Beauty Bless You - O(n*2^n) time | O(n*2^n) space
def powerset(array):
    sets, stack, p_cur = [], [], False
    while True:
        if p_cur is not None:
            if len(stack) == len(array):
                sets.append([array[_] for _ in range(len(array)) if stack[_]])
                p_cur = None
            else:
                stack.append(p_cur)
        elif stack:
            if not stack[-1]:
                stack[-1], p_cur = True, False
            else:
                stack.pop()
        else:
            break
    return sets
