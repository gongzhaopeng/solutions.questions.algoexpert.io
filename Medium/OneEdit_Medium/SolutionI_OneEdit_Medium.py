# Algorithmic Beauty Bless You - O(n) time | O(1) space
def oneEdit(stringOne, stringTwo):
    if len(stringOne) < len(stringTwo):
        stringOne, stringTwo = stringTwo, stringOne
    if len(stringOne) - len(stringTwo) > 1:
        return False
    edited, i, j = False, 0, 0
    while j < len(stringTwo):
        if stringOne[i] != stringTwo[j]:
            if edited:
                return False
            edited = True
            if len(stringOne) != len(stringTwo):
                i += 1
                continue
        i, j = i + 1, j + 1
    return True
