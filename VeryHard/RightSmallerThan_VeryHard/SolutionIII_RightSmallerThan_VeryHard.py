def rightSmallerThan(array):
    if not array:
        return []
    count_array = array[:]
    max_index = len(array) - 1
    count_array[max_index] = 0
    bst = _SpecialBST(max_index, array[max_index])
    for i in reversed(range(max_index)):
        bst.insert(i, array[i], count_array)
    return count_array


class _SpecialBST:
    def __init__(self, index, value):
        self.index = index
        self.value = value
        self.left_subtree_size = 0
        self.left, self.right = None, None

    def insert(self, index, value, count_array):
        new_node = _SpecialBST(index, value)
        count_array[index] = 0
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
                count_array[index] += parent.left_subtree_size
                if value != parent.value:
                    count_array[index] += 1
                if parent.right:
                    parent = parent.right
                else:
                    parent.right = new_node
                    break
