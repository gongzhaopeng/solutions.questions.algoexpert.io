# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
# Algorithmic Beauty Bless You - O(n) time | O(d) space
def productSum(array):
    stack = []
    root = current = [0, 1, array, 0]  # [summ, depth, obj, p_visiting]
    while True:
        if current:
            _, depth, obj, _ = current
            if type(obj) is int:
                stack[-1][0] += obj
                current = None
                continue
            stack.append(current)
            current = [0, depth + 1, obj[0], 0]
        elif stack:
            stack[-1][-1] += 1
            summ, depth, arr, p_visiting = stack[-1]
            if p_visiting < len(arr):
                current = [0, depth + 1, arr[p_visiting], 0]
            else:
                popped = stack.pop()
                popped[0] = summ * depth
                if stack:
                    stack[-1][0] += popped[0]
        else:
            break
    return root[0]
