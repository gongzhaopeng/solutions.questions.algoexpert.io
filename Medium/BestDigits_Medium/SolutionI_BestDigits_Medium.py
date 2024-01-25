# Algorithmic Beauty Bless You - O(n) time | O(n) space
def bestDigits(number, numDigits):
    stack, p_head, largest_number = [], 0, []
    for i in range(len(number)):
        while len(stack) > p_head and number[i] > stack[-1]:
            stack.pop()
        stack.append(number[i])
        if i >= numDigits:
            largest_number.append(stack[p_head])
            p_head += 1
    return ''.join(largest_number)
