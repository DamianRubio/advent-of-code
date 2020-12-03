from functools import reduce

input_file = '2020/03/input.txt'

with open(input_file) as f:
    trees_map = [list(i) for i in f.read().splitlines()]


def calculates_trees_in_trajectory(trees_map, x_movement, y_movement):
    y_end = len(trees_map)
    x_pos, y_pos = 0, 0
    trees_found = 0
    while y_pos < y_end:
        if trees_map[y_pos][x_pos] == "#":
            trees_found += 1
        if x_pos >= len(trees_map[0]) - x_movement:
            x_pos = x_pos + x_movement - len(trees_map[0])
        else:
            x_pos += x_movement
        y_pos += y_movement
    return trees_found
    pass


def solve_part_one():
    return calculates_trees_in_trajectory(trees_map, 3, 1)


def solve_part_two():
    movements = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees_per_trajectory = []

    for x_movement, y_movement in movements:
        trees_per_trajectory.append(calculates_trees_in_trajectory(
            trees_map, x_movement, y_movement))

    return reduce(lambda x, y: x*y, trees_per_trajectory)


print("Part one. The number of trees found is: {}.".format(solve_part_one()))
print("Part two. The number of trees found is: {}.".format(solve_part_two()))
