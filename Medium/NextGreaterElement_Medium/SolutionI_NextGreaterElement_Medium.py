# Algorithmic Beauty Bless You - O(n) time | O(n) space
def nextGreaterElement(array):
    new_array, stack = [-1] * len(array), []
    for i, e in enumerate(array):
        while stack and e > array[stack[-1]]:
            new_array[stack.pop()] = e
        stack.append(i)
    for e in array:
        while e > array[stack[-1]]:
            new_array[stack.pop()] = e
    return new_array
