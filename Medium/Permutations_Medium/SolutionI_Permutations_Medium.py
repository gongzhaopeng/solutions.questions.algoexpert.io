# Algorithmic Beauty Bless You - O(n*n!) time | O(n*n!) space
def getPermutations(array):
    permutations, selective, stack, go_down = [], set(array), [], len(array) > 0
    while True:
        if go_down:
            stack.append([selective.pop(), list(selective)])
            if not selective:
                permutations.append([_[0] for _ in stack])
                go_down = False
        elif stack:
            v, candidates = stack[-1]
            selective.add(v)
            if candidates:
                stack[-1][0] = candidates.pop()
                selective.remove(stack[-1][0])
                go_down = True
            else:
                stack.pop()
        else:
            break
    return permutations
