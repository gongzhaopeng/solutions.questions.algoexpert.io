def subarraySort(array):
    asc_end = 1
    while asc_end < len(array):
        if array[asc_end] < array[asc_end - 1]:
            break
        asc_end += 1
    if asc_end == len(array):
        return [-1, -1]
    asc_end -= 1
    des_start = len(array) - 2
    while True:
        if array[des_start] > array[des_start + 1]:
            break
        des_start -= 1
    des_start += 1
    max_unsorted = array[asc_end]
    min_unsorted = array[des_start]
    for i in range(asc_end + 1, des_start):
        elem = array[i]
        if elem > max_unsorted:
            max_unsorted = elem
        elif elem < min_unsorted:
            min_unsorted = elem
    start_to_sort = 0
    while array[start_to_sort] <= min_unsorted:
        start_to_sort += 1
    end_to_sort = len(array) - 1
    while array[end_to_sort] >= max_unsorted:
        end_to_sort -= 1
    return [start_to_sort, end_to_sort]
