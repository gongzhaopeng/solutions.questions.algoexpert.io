import math
from collections import deque


# Algorithmic Beauty Bless You - O(n * m) time | O(n * m) space
def knightConnection(knightA, knightB):
    if knightA == knightB:
        return 0
    candi_moves = [[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]
    right_ward_moves = candi_moves[-2:] + candi_moves[0:2]
    left_ward_moves = candi_moves[2:6]
    upward_moves = candi_moves[0:4]
    downward_moves = candi_moves[-4:]
    top_right_ward_moves = candi_moves[-1:] + candi_moves[:3]
    bottom_right_ward_moves = candi_moves[-3:] + candi_moves[:1]
    top_left_ward_moves = candi_moves[1:5]
    bottom_left_ward_moves = candi_moves[3:7]
    queue = deque([[knightA[0], knightA[1], 0]])
    visited = {(knightA[0], knightA[1])}
    while True:
        cur_node = queue.popleft()
        if cur_node[1] == knightB[1]:
            if cur_node[0] < knightB[0]:
                moves = right_ward_moves
            else:
                moves = left_ward_moves
        elif cur_node[0] == knightB[0]:
            if cur_node[1] < knightB[1]:
                moves = upward_moves
            else:
                moves = downward_moves
        elif cur_node[0] < knightB[0]:
            if cur_node[1] < knightB[1]:
                moves = top_right_ward_moves
            else:
                moves = bottom_right_ward_moves
        else:
            if cur_node[1] < knightB[1]:
                moves = top_left_ward_moves
            else:
                moves = bottom_left_ward_moves
        for move in moves:
            next_node = [cur_node[0] + move[0], cur_node[1] + move[1]]
            ne_node_tuple = (next_node[0], next_node[1])
            if ne_node_tuple in visited:
                continue
            next_node.append(cur_node[2] + 1)
            if next_node[:2] == knightB:
                return math.ceil(next_node[2] / 2)
            queue.append(next_node)
            visited.add(ne_node_tuple)
