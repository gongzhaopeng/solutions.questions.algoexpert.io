def subarraySort(array):
    down_uo_peak = float('inf')
    up_uo_peak = float('-inf')
    if array[len(array) - 1] < array[len(array) - 2]:
        down_uo_peak = array[len(array) - 1]
    if array[1] < array[0]:
        up_uo_peak = array[0]
    for i in range(1, len(array) - 1):
        if array[i] < array[i - 1]:
            down_uo_peak = min(down_uo_peak, array[i])
        elif array[i + 1] < array[i]:
            up_uo_peak = max(up_uo_peak, array[i])
    if down_uo_peak == float('inf'):
        return [-1, -1]
    start_to_sort = 0
    while down_uo_peak >= array[start_to_sort]:
        start_to_sort += 1
    end_to_sort = len(array) - 1
    while up_uo_peak <= array[end_to_sort]:
        end_to_sort -= 1
    return [start_to_sort, end_to_sort]
