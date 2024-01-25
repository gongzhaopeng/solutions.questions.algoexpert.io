def moveElementToEnd(array, toMove):
    search_index = 0
    target_index = len(array) - 1
    while search_index < target_index:
        if array[target_index] == toMove:
            target_index -= 1
            continue
        if array[search_index] == toMove:
            array[search_index] = array[target_index]
            array[target_index] = toMove
            target_index -= 1
        search_index += 1
    return array
