from itertools import permutations

input_file = '2020/17/input.txt'

STATE_ACTIVE = '#'
STATE_INACTIVE = '.'

initial_grid = [list(line.strip()) for line in open(input_file).readlines()]
intital_grid_3d = [initial_grid]

directions = set(list(permutations([-1, 0, 1, -1, 0, 1, -1, 0, 1], 3)))
directions.remove((0, 0, 0))


def count_by_state(initial_grid_3d, count_state=STATE_ACTIVE):
    counter = 0
    for z_dim in intital_grid_3d:
        for x_dim in z_dim:
            for element in x_dim:
                if element == count_state:
                    counter += 1
    return counter


def solve_part_one(initial_grid_3d, n_loops=6):
    while n_loops > 0:
        pass
        n_loops -= 1
    return count_by_state(intital_grid_3d)


print(intital_grid_3d, len(directions))
print('Part one. The number of cubes in the active state after the sixth cycle is: {}.'.format(None))
