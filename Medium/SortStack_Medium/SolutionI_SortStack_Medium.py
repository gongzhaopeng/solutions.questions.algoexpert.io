# Algorithmic Beauty Bless You - O(n^2) time | O(n) space
def sortStack(stack):
    if stack:
        top = stack.pop()
        sortStack(stack)
        sift_down(top, stack)
    return stack


def sift_down(v, stack):
    if stack and v < stack[-1]:
        top = stack.pop()
        sift_down(v, stack)
        v = top
    stack.append(v)
