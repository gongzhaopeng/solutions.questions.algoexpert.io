def fourNumberSum(array, targetSum):
    head_pair_sums = {}
    quadruplets = []
    for third_index in range(1, len(array) - 1):
        for fourth_index in range(third_index + 1, len(array)):
            tail_pair_sum = array[third_index] + array[fourth_index]
            difference = targetSum - tail_pair_sum
            if difference in head_pair_sums:
                for head_pair in head_pair_sums[difference]:
                    quadruplets.append(head_pair + [array[third_index], array[fourth_index]])
        second_index = third_index
        for first_index in range(second_index):
            head_pair_sum = array[first_index] + array[second_index]
            if head_pair_sum not in head_pair_sums:
                head_pair_sums[head_pair_sum] = [[array[first_index], array[second_index]]]
            else:
                head_pair_sums[head_pair_sum].append([array[first_index], array[second_index]])
    return quadruplets
