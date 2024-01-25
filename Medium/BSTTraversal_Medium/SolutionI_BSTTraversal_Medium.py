# Algorithmic Beauty Bless You - O(n) time | O(n) space
def inOrderTraverse(tree, array):
    current, stack = tree, []
    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            popped = stack.pop()
            array.append(popped.value)
            current = popped.right
        else:
            break
    return array


# Algorithmic Beauty Bless You - O(n) time | O(n) space
def preOrderTraverse(tree, array):
    current, stack = tree, []
    while True:
        if current:
            array.append(current.value)
            stack.append(current)
            current = current.left
        elif stack:
            popped = stack.pop()
            current = popped.right
        else:
            break
    return array


# Algorithmic Beauty Bless You - O(n) time | O(n) space
def postOrderTraverse(tree, array):
    current, stack = [tree, 0], []
    while True:
        if current[0]:
            stack.append(current)
            current = [current[0].left, 0]
        elif stack:
            stack[-1][-1] += 1
            node, p_visiting = stack[-1]
            if p_visiting > 1:
                stack.pop()
                array.append(node.value)
                current = [None]
            else:
                current = [node.right, 0]
        else:
            break
    return array
