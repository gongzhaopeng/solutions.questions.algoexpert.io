# Algorithmic Beauty Bless You - O(height) time | O(maxSteps) space
def staircaseTraversal(height, maxSteps):
    dpt = [0] * (maxSteps + 1)
    dpt[0], dpt[1], index = 1, 1, 1
    for h in range(2, height + 1):
        index = h % (maxSteps + 1)
        dpt[index] = 2 * dpt[index - 1] - dpt[index]
    return dpt[index]
