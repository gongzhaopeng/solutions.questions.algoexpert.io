def sortedSquaredArray(array):
    if len(array) == 1:
        return [array[0] ** 2]
    squared_array = [None for _ in array]
    forward_index = 0
    array[forward_index] **= 2
    backward_index = len(array) - 1
    array[backward_index] **= 2
    for target_index in reversed(range(2, len(array))):
        if array[forward_index] > array[backward_index]:
            squared_array[target_index] = array[forward_index]
            forward_index += 1
            array[forward_index] **= 2
        else:
            squared_array[target_index] = array[backward_index]
            backward_index -= 1
            array[backward_index] **= 2
    if array[forward_index] > array[backward_index]:
        squared_array[0:2] = [array[backward_index], array[forward_index]]
    else:
        squared_array[0:2] = [array[forward_index], array[backward_index]]
    return squared_array
