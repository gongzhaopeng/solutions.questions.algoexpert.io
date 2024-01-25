# Algorithmic Beauty Bless You - O(VE)=O(n^3) time | O(n) space
def detectArbitrage(exchangeRates):
    size = len(exchangeRates)
    dpt = [float('-inf')] * size
    dpt[0], updated = exchangeRates[0][0], False
    for _ in range(size):
        updated = False
        for i in range(size):
            for j in range(size):
                new_rate = dpt[i] * exchangeRates[i][j]
                if new_rate <= dpt[j]:
                    continue
                dpt[j], updated = new_rate, True
        if not updated:
            return False
    return updated
