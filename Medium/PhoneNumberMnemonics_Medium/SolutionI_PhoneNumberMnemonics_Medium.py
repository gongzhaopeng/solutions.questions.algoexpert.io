mapping = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']


# Algorithmic Beauty Bless You - O(n*4^n) time | O(n*4^n) space
def phoneNumberMnemonics(phoneNumber):
    phoneNumber = list(map(int, phoneNumber))
    mnemonics, stack, go_down = [], [], True
    while True:
        if go_down:
            if len(stack) == len(phoneNumber):
                mnemonics.append(''.join(mapping[phoneNumber[i]][j] for i, j in enumerate(stack)))
                go_down = False
                continue
            stack.append(0)
        elif stack:
            stack[-1] += 1
            if stack[-1] < len(mapping[phoneNumber[len(stack) - 1]]):
                go_down = True
            else:
                stack.pop()
        else:
            break
    return mnemonics
