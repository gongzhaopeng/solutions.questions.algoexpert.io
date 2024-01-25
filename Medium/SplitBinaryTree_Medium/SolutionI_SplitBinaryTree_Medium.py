# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Algorithmic Beauty Bless You - O(n) time | O(h) space
def splitBinaryTree(tree):
    summary = get_sum(tree)
    return check_valid_split(tree, summary / 2)


def get_sum(tree):
    summary, current, stack = 0, tree, []
    while True:
        if current:
            stack.append(current)
            summary += current.value
            current = current.left
        elif stack:
            popped = stack.pop()
            current = popped.right
        else:
            break
    return summary


def check_valid_split(tree, exp_sum):
    current, stack = [tree, 0, None], []
    while True:
        if current[0]:
            stack.append(current)
            current[-1] = current[0].value
            current = [current[0].left, 0, None]
        elif stack:
            stack[-1][1] += 1
            node, p_visiting, summary = stack[-1]
            if p_visiting > 1:
                if summary == exp_sum:
                    return exp_sum
                stack.pop()
                if stack:
                    stack[-1][-1] += summary
            else:
                current = [node.right, 0, None]
        else:
            break
    return 0
