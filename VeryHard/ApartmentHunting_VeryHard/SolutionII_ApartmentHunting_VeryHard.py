def apartmentHunting(blocks, reqs):
    dis_up_bounds = [-1 for _ in blocks]
    for req in reqs:
        refresh_dis_up_bounds_per_req(blocks, req, dis_up_bounds)
    return find_index_with_min_value(dis_up_bounds)


def refresh_dis_up_bounds_per_req(blocks, req, dis_up_bounds):
    block_count = len(blocks)
    min_distances = [0 for _ in range(block_count)]
    closest_pos = -block_count
    for i in range(block_count):
        if blocks[i][req]:
            closest_pos = i
        min_distances[i] = i - closest_pos
    closest_pos = 2 * block_count
    for i in reversed(range(block_count)):
        if blocks[i][req]:
            closest_pos = i
        dis_up_bounds[i] = max(
            dis_up_bounds[i],
            min(min_distances[i], closest_pos - i))


def find_index_with_min_value(array):
    index = 0
    min_value = array[0]
    for i in range(1, len(array)):
        if array[i] < min_value:
            min_value = array[i]
            index = i
    return index
