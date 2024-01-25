def rightSmallerThan(array):
    def fill_in_counts():
        nodes = [bst]
        while nodes:
            node = nodes.pop()
            count_array[node.index] = node.rl_count
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)

    if not array:
        return []
    count_array = array[:]
    max_index = len(array) - 1
    bst = _SpecialBST(max_index, array[max_index])
    for i in reversed(range(max_index)):
        bst.insert(i, array[i])
    fill_in_counts()
    return count_array


class _SpecialBST:
    def __init__(self, index, value):
        self.index = index
        self.value = value
        self.rl_count = 0
        self.left_subtree_size = 0
        self.left, self.right = None, None

    def insert(self, index, value):
        new_node = _SpecialBST(index, value)
        parent = self
        while True:
            if value < parent.value:
                parent.left_subtree_size += 1
                if parent.left:
                    parent = parent.left
                else:
                    parent.left = new_node
                    break
            else:
                new_node.rl_count += parent.left_subtree_size
                if value != parent.value:
                    new_node.rl_count += 1
                if parent.right:
                    parent = parent.right
                else:
                    parent.right = new_node
                    break
