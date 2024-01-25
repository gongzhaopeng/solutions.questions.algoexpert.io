import math

base_square_size = 5
base_cases = [[]] * base_square_size
base_cases[4] = [2, 3, 2, 3, 4]
base_cases[3] = [3, 2, 3, 2, 3]
base_cases[2] = [2, 1, 4, 3, 2]
base_cases[1] = [3, 2, 1, 2, 3]
base_cases[0] = [0, 3, 2, 3, 2]


# Algorithmic Beauty Bless You - O(1) time | O(1) space
def knightConnection(knightA, knightB):
    return math.ceil(determine_steps(knightA, knightB) / 2)


def determine_steps(knight_a, knight_b):
    x, y = normalize_positions(knight_a, knight_b)
    if x < base_square_size:
        return base_cases[x][y]
    ref_x = base_square_size - 1
    steps = 0
    slope = y / x
    if slope > 1 / 2:
        delta_steps = min(math.ceil((x - ref_x) / 2), x - y)
        x, y = x - 2 * delta_steps, y - delta_steps
        steps += delta_steps
        x_to_dec = x - ref_x
        if x_to_dec > 0:
            double_steps_count = x_to_dec // 3
            delta_steps = 2 * double_steps_count
            x, y = x - 3 * double_steps_count, y - 3 * double_steps_count
            remain = x_to_dec % 3
            if remain == 1:
                delta_steps += 1
                x, y = x - 1, y - 2
            elif remain == 2:
                delta_steps += 2
                x, y = x - 3, y - 3
            steps += delta_steps
    else:
        delta_steps = min(math.ceil((x - ref_x) / 2), y)
        x, y = x - 2 * delta_steps, y - delta_steps
        steps += delta_steps
        x_to_dec = x - ref_x
        if x_to_dec > 0:
            double_steps_count = x_to_dec // 4
            delta_steps = 2 * double_steps_count
            x -= 4 * double_steps_count
            remain = x % 4
            if remain == 1 or remain == 2:
                delta_steps += 1
                x, y = x - 2, y + 1
            elif remain == 3:
                delta_steps += 2
                x -= 4
            steps += delta_steps
    return steps + base_cases[x][y]


def normalize_positions(knight_a, knight_b):
    x, y = abs(knight_b[0] - knight_a[0]), abs(knight_b[1] - knight_a[1])
    if y > x:
        x, y = y, x
    return x, y
