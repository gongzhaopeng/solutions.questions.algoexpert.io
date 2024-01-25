# Algorithmic Beauty Bless You - O(n) time | O(logn) space
def maxPathSum(tree):
    return path_info(tree)[1]


def path_info(tree):
    max_to_join, max_sum = 0, float('-inf')
    if not tree:
        return max_to_join, max_sum
    l_to_join, l_max_sum = path_info(tree.left)
    r_to_join, r_max_sum = path_info(tree.right)
    max_to_join = max(max(l_to_join, r_to_join) + tree.value, tree.value)
    max_sum = max(l_to_join + tree.value + r_to_join, max_to_join, l_max_sum, r_max_sum)
    return max_to_join, max_sum
