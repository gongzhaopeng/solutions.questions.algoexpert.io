# Algorithmic Beauty Bless You - O(nlogn) time | O(n) space
def taskAssignment(k, tasks):
    sorted_indices = list(range(len(tasks)))
    sorted_indices.sort(key=lambda _: tasks[_])
    return [[sorted_indices[i], sorted_indices[-(i + 1)]] for i in range(k)]
