# Algorithmic Beauty Bless You - O(w * h) time | O(min(w, h)) space
def numberOfWaysToTraverseGraph(width, height):
    if height < width:
        height, width = width, height
    dpt = [1] * width
    for h in range(1, height):
        for w in range(1, width):
            dpt[w] = dpt[w] + dpt[w - 1]
    return dpt[-1]
