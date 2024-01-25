def fourNumberSum(array, targetSum):
    array.sort()
    quadruplets = []
    for first_index in range(len(array) - 3):
        without_first = targetSum - array[first_index]
        for second_index in range(first_index + 1, len(array) - 2):
            rest = without_first - array[second_index]
            third_index = second_index + 1
            fourth_index = len(array) - 1
            while third_index < fourth_index:
                fill_in = array[third_index] + array[fourth_index]
                if fill_in < rest:
                    third_index += 1
                elif fill_in > rest:
                    fourth_index -= 1
                else:
                    quadruplets.append([
                        array[first_index],
                        array[second_index],
                        array[third_index],
                        array[fourth_index]
                    ])
                    third_index += 1
                    fourth_index -= 1
    return quadruplets
