def apartmentHunting(blocks, reqs):
    distances = []
    block_count = len(blocks)
    req_count = len(reqs)
    f_dis = [block_count] * req_count
    b_dis = f_dis.copy()
    for f_index in range(block_count):
        forward = blocks[f_index]
        for req_index in range(req_count):
            f_dis[req_index] = 0 if forward[reqs[req_index]] else f_dis[req_index] + 1
        distances.append(f_dis.copy())
    for b_index in reversed(range(block_count)):
        backward = blocks[b_index]
        for req_index in range(req_count):
            b_dis[req_index] = 0 if backward[reqs[req_index]] else b_dis[req_index] + 1
            distances[b_index][req_index] = min(distances[b_index][req_index], b_dis[req_index])
    optimal_index = -1
    optimal_dis = block_count
    for index in range(block_count):
        cur_max_dis = max(distances[index])
        if cur_max_dis < optimal_dis:
            optimal_index = index
            optimal_dis = cur_max_dis
    return optimal_index
