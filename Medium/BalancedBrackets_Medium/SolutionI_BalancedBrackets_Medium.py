# Algorithmic Beauty Bless You - O(n) time | O(n) space
def balancedBrackets(string):
    openings, closings, stack = '([{', ')]}', []
    for c in string:
        if c in openings:
            stack.append(c)
            continue
        try:
            if openings[closings.index(c)] != stack.pop():
                return False
        except ValueError:
            pass
        except IndexError:
            return False
    return not stack
