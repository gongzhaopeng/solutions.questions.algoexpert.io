from math import factorial


# Algorithmic Beauty Bless You - O(w+h) time | O(1) space
def numberOfWaysToTraverseGraph(width, height):
    return factorial(width - 1 + height - 1) / (factorial(width - 1) * (factorial(height - 1)))
