def isMonotonic(array):
    if not array:
        return True
    exp_trend = array[len(array) - 1] - array[0]
    if exp_trend > 0:
        breaking = (lambda index: array[index] < array[index - 1])
    elif exp_trend < 0:
        breaking = (lambda index: array[index] > array[index - 1])
    else:
        breaking = (lambda index: array[index] != array[0])
    for i in range(1, len(array)):
        if breaking(i):
            return False
    return True
