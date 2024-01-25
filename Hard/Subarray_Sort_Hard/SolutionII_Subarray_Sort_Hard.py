def subarraySort(array):
    down_uo_peak = float('inf')
    up_uo_peak = float('-inf')
    count = len(array)
    pre = array[count - 1] - array[count - 2]
    if pre < 0:
        down_uo_peak = array[count - 1]
    pre = array[1] - array[0]
    if pre < 0:
        up_uo_peak = array[0]
    for i in range(1, count - 1):
        post = array[i + 1] - array[i]
        if pre < 0:
            if not post < 0:
                down_uo_peak = min(down_uo_peak, array[i])
        elif post < 0:
            up_uo_peak = max(up_uo_peak, array[i])
        pre = post
    if down_uo_peak == float('inf'):
        return [-1, -1]
    start_to_sort = 0
    while down_uo_peak >= array[start_to_sort]:
        start_to_sort += 1
    end_to_sort = count - 1
    while up_uo_peak <= array[end_to_sort]:
        end_to_sort -= 1
    return [start_to_sort, end_to_sort]
