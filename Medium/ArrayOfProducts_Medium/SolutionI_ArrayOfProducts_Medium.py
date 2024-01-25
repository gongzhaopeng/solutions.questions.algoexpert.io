# Algorithmic Beauty Bless You - O(n) time | O(n) space
def arrayOfProducts(array):
    products, end_products = array[:], array[:]
    last_index = len(array) - 1
    end_products[last_index] = array[last_index]
    for i in reversed(range(1, last_index)):
        end_products[i] = array[i] * end_products[i + 1]
    products[0] = end_products[1]
    for i in range(1, last_index):
        products[i] = end_products[i - 1] * end_products[i + 1]
        end_products[i] = end_products[i - 1] * array[i]
    products[last_index] = end_products[last_index - 1]
    return products
