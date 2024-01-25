# Algorithmic Beauty Bless You - O(n) time | O(1) space
def validStartingCity(distances, fuel, mpg):
    non_neg_sum_head, non_neg_sum = 0, 0
    for i, dis in enumerate(distances):
        non_neg_sum += fuel[i] * mpg - dis
        if non_neg_sum < 0:
            non_neg_sum_head, non_neg_sum = i + 1, 0
    return non_neg_sum_head
