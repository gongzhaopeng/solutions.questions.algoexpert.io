# Algorithmic Beauty Bless You - O(n) time | O(n) space
def arrayOfProducts(array):
    products = array[:]
    products[0] = 1
    for i in range(1, len(array)):
        products[i] = array[i - 1] * products[i - 1]
    r_end_product = 1
    for i in reversed(range(len(array))):
        products[i] = products[i] * r_end_product
        r_end_product *= array[i]
    return products
