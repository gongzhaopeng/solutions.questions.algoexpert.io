# Algorithmic Beauty Bless You - O(n^3) time | O(n^2) space
def detectArbitrage(exchangeRates):
    size = len(exchangeRates)
    parents = [[_] * size for _ in range(size)]
    for k in range(size):
        for i in range(size):
            for j in range(size):
                new_rate = exchangeRates[i][k] * exchangeRates[k][j]
                if new_rate <= exchangeRates[i][j]:
                    continue
                if i == j:
                    path = construct_path(parents, i, parents[k][j])
                    return True
                exchangeRates[i][j] = new_rate
                parents[i][j] = parents[k][j]
    return False


def construct_path(parents, i, j):
    path = [i]
    while i != j:
        path.append(j)
        j = parents[i][j]
    path.append(i)
    path.reverse()
    return path
