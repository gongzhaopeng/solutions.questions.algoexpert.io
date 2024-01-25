import operator


# Algorithmic Beauty Bless You - O(n) time | O(n) space
def reversePolishNotation(tokens):
    ops, stack = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}, []
    for tok in tokens:
        op = ops.get(tok)
        if op:
            b, a = stack.pop(), stack.pop()
            tok = op(a, b)
        stack.append(int(tok))
    return int(stack[-1])
