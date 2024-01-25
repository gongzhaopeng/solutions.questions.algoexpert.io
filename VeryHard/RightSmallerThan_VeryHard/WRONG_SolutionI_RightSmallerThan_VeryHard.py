import random


def rightSmallerThan(array):
    def compare(a, b):
        diff = a[0] - b[0] or a[1] - b[1]
        return 1 if diff > 0 else -1 if diff < 0 else 0

    def count_right_equals():
        p_to_count, to_count, count, p_cur = 0, node_arr[0][0], 1, 1
        while p_cur < len(node_arr):
            if node_arr[p_cur][0] == to_count:
                count, p_cur = count + 1, p_cur + 1
                continue
            for i in range(p_to_count, p_cur):
                count -= 1
                node_arr[i][2] = count
            p_to_count, to_count, count, p_cur = p_cur, node_arr[p_cur][0], 1, p_cur + 1

    count_arr = [None for _ in array]
    node_arr = [[elem, i, 0] for i, elem in enumerate(array)]
    quick_sort(node_arr, 0, len(node_arr), compare)
    count_right_equals()
    for i, node in enumerate(node_arr):
        # --- THIS IS OF WRONG LOGIC ---
        count_arr[node[1]] = i - count_arr[node[1]]


def quick_sort(array, p_start, p_end,
               cmp=lambda a, b: 1 if a > b else -1 if a < b else 0):
    if p_end - p_start < 2:
        return
    p_ref = random.randrange(p_start, p_end)
    referee = array[p_ref]
    cur, step, p_swap_to = p_start, 1, p_end - 1
    array[p_ref] = array[p_swap_to]
    while cur != p_swap_to:
        if cmp(array[cur], referee) == step:
            array[p_swap_to] = array[cur]
            step = -step
            cur, p_swap_to = p_swap_to + step, cur
        else:
            cur += step
    array[p_swap_to] = referee
    quick_sort(array, p_start, p_swap_to, cmp)
    quick_sort(array, p_swap_to + 1, p_end, cmp)
