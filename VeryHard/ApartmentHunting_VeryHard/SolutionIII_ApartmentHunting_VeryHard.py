def apartmentHunting(blocks, reqs):
    block_count = len(blocks)
    optimal_index = -1
    optimal_dis = block_count
    for i in range(block_count):
        dis_up_bound = -1
        for req in reqs:
            min_dis = block_count
            for j in range(block_count):
                if blocks[j][req]:
                    min_dis = min(min_dis, abs(i - j))
            dis_up_bound = max(dis_up_bound, min_dis)
        if dis_up_bound < optimal_dis:
            optimal_dis = dis_up_bound
            optimal_index = i
    return optimal_index
