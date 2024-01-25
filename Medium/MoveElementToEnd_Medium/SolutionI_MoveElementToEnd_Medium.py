def moveElementToEnd(array, toMove):
    target_index = len(array) - 1
    key_index = 0
    while True:
        while target_index > key_index:
            if array[target_index] != toMove:
                break
            target_index -= 1
        while key_index < target_index:
            if array[key_index] == toMove:
                break
            key_index += 1
        if target_index <= key_index:
            break
        array[key_index] = array[target_index]
        array[target_index] = toMove
        target_index -= 1
        key_index += 1
    return array
