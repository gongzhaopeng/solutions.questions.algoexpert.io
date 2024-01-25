# Algorithmic Beauty Bless You - O(n^3) time | O(1) space
def detectArbitrage(exchangeRates):
    size = len(exchangeRates)
    for k in range(size):
        for i in range(size):
            for j in range(size):
                new_rate = exchangeRates[i][k] * exchangeRates[k][j]
                if new_rate <= exchangeRates[i][j]:
                    continue
                if i == j:
                    return True
                exchangeRates[i][j] = new_rate
    return False
