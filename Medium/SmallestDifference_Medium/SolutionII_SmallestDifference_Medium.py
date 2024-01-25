def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    pair = [arrayOne[0], arrayTwo[0]]
    smallest = abs(pair[0] - pair[1])
    index_one = 0
    index_two = 0
    while True:
        elem_one = arrayOne[index_one]
        elem_two = arrayTwo[index_two]
        if elem_one > elem_two:
            diff = elem_one - elem_two
            index_two += 1
            halt = index_two >= len(arrayTwo)
        elif elem_one < elem_two:
            diff = elem_two - elem_one
            index_one += 1
            halt = index_one >= len(arrayOne)
        else:
            diff = 0
            halt = True
        if diff < smallest:
            smallest = diff
            pair = [elem_one, elem_two]
        if halt:
            break
    return pair
