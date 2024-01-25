from itertools import islice


# Algorithmic Beauty Bless You - O(n) time | O(n) space
def bestDigits(number, numDigits):
    stack = ['9']
    for digit in number:
        while numDigits and digit > stack[-1]:
            numDigits -= 1
            stack.pop()
        stack.append(digit)
    return ''.join(islice(stack, 1, len(stack) - numDigits))
