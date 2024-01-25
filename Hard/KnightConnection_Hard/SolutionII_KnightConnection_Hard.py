import math
from collections import deque

candi_moves = [[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]
right_ward_moves = candi_moves[-2:] + candi_moves[0:2]
left_ward_moves = candi_moves[2:6]
upward_moves = candi_moves[0:4]
downward_moves = candi_moves[-4:]
top_right_ward_moves = candi_moves[-1:] + candi_moves[:3]
bottom_right_ward_moves = candi_moves[-3:] + candi_moves[:1]
top_left_ward_moves = candi_moves[1:5]
bottom_left_ward_moves = candi_moves[3:7]


# Algorithmic Beauty Bless You - o(n * m) time | o(n * m) space
def knightConnection(knightA, knightB):
    queue = deque([[knightA[0], knightA[1], 0]])
    visited = {(knightA[0], knightA[1])}
    possible_min_steps = float('inf')
    while queue:
        cur_node = queue.popleft()
        n, m = abs(cur_node[0] - knightB[0]), abs(cur_node[1] - knightB[1])
        if n < m:
            n, m = m, n
        rough_down_bound_steps = determiner_rough_down_bound_steps(n, m)
        if rough_down_bound_steps + cur_node[2] >= possible_min_steps:
            continue
        a_good_steps = find_a_good_steps(n, m)
        possible_min_steps = min(possible_min_steps, a_good_steps + cur_node[2])
        if rough_down_bound_steps == a_good_steps:
            continue
        moves = determine_possible_movies(cur_node, knightB)
        for move in moves:
            next_node = [cur_node[0] + move[0], cur_node[1] + move[1]]
            ne_node_tuple = (next_node[0], next_node[1])
            if ne_node_tuple in visited:
                continue
            next_node.append(cur_node[2] + 1)
            queue.append(next_node)
            visited.add(ne_node_tuple)
    return math.ceil(possible_min_steps / 2)


def determiner_rough_down_bound_steps(big_dim, small_dim):
    if small_dim == 0:
        return math.ceil(big_dim / 2)
    else:
        return math.ceil((big_dim + small_dim) / 3)


def find_a_good_steps(big_dim, small_dim):
    up_bound_steps = 0
    diff = big_dim - small_dim
    delta_steps = min(diff, small_dim)
    big_dim, small_dim = big_dim - delta_steps * 2, small_dim - delta_steps
    if big_dim < small_dim:
        big_dim, small_dim = small_dim, big_dim
    up_bound_steps += delta_steps
    if small_dim:  # In this case, it is a square.
        up_bound_steps += 2 * (small_dim // 3)
        remain = small_dim % 3
        if remain == 1:
            up_bound_steps += 2
        elif remain == 2:
            up_bound_steps += 4
    else:
        up_bound_steps += 2 * (big_dim // 4)
        remain = big_dim % 4
        if remain == 1:
            up_bound_steps += 3
        elif remain == 2:
            up_bound_steps += 2
        elif remain == 3:
            up_bound_steps += 3
    return up_bound_steps


def determine_possible_movies(cur_pos, target_pos):
    if cur_pos[1] == target_pos[1]:
        if cur_pos[0] < target_pos[0]:
            moves = right_ward_moves
        else:
            moves = left_ward_moves
    elif cur_pos[0] == target_pos[0]:
        if cur_pos[1] < target_pos[1]:
            moves = upward_moves
        else:
            moves = downward_moves
    elif cur_pos[0] < target_pos[0]:
        if cur_pos[1] < target_pos[1]:
            moves = top_right_ward_moves
        else:
            moves = bottom_right_ward_moves
    else:
        if cur_pos[1] < target_pos[1]:
            moves = top_left_ward_moves
        else:
            moves = bottom_left_ward_moves
    return moves
