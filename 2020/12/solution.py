from collections import defaultdict
from copy import deepcopy

input_file = '2020/12/input.txt'

ship_instructions = open(input_file).read().strip('\n').split('\n')
ordered_positions = ['north', 'east', 'south', 'west']


def compute_manhattan_distance(movement_dict):
    return abs(movement_dict['north']) + abs(movement_dict['east'])


def move_south(movement_dict, amount):
    movement_dict['north'] -= amount
    return movement_dict


def move_west(movement_dict, amount):
    movement_dict['east'] -= amount
    return movement_dict


def move_forward(movement_dict, facing, amount):
    if facing == 'east' or facing == 'north':
        movement_dict[facing] += amount
    elif facing == 'south':
        movement_dict = move_south(movement_dict, amount)
    elif facing == 'west':
        movement_dict = move_west(movement_dict, amount)
    return movement_dict


def rotate_ship(facing, rotation_side, degrees):
    postions_to_rotate = degrees // 90
    starting_pos = ordered_positions.index(facing)

    if rotation_side == 'L':
        return ordered_positions[starting_pos-postions_to_rotate]
    elif rotation_side == 'R':
        index_after_rotation = starting_pos+postions_to_rotate
        if index_after_rotation >= len(ordered_positions):
            index_after_rotation = index_after_rotation - \
                len(ordered_positions)
        return ordered_positions[index_after_rotation]


def parse_movement(ship_instructions):
    movement_dict = defaultdict(int)
    facing = 'east'

    for instruction in ship_instructions:
        if instruction[0] == 'F':
            movement_dict = move_forward(
                movement_dict, facing, int(instruction[1:]))
        elif instruction[0] == 'N':
            movement_dict['north'] += int(instruction[1:])
        elif instruction[0] == 'S':
            movement_dict = move_south(movement_dict, int(instruction[1:]))
        elif instruction[0] == 'E':
            movement_dict['east'] += int(instruction[1:])
        elif instruction[0] == 'W':
            movement_dict = move_west(movement_dict, int(instruction[1:]))
        elif instruction[0] == 'L' or instruction[0] == 'R':
            facing = rotate_ship(facing, instruction[0], int(instruction[1:]))
    return movement_dict


def move_forward_by_waypoint(movement_dict, waypoint_dict, amount):
    movement_dict['north'] += waypoint_dict['north'] * amount
    movement_dict['east'] += waypoint_dict['east'] * amount

    return movement_dict


def move_waypoint(movement_dict, direction, amount):
    if direction == 'north':
        movement_dict['north'] += amount
    elif direction == 'south':
        movement_dict = move_south(movement_dict, amount)
    elif direction == 'east':
        movement_dict['east'] += amount
    elif direction == 'west':
        movement_dict = move_west(movement_dict, amount)
    return movement_dict


def rotate_waypoint_around_ship(waypoint_dict, rotation_side, degrees):
    waypoint_dict_copy = {'north': 0, 'east': 0}
    postions_to_rotate = degrees // 90

    if rotation_side == 'L':
        for pos in ['east', 'north']:
            starting_pos = ordered_positions.index(pos)
            converts_to = ordered_positions[starting_pos-postions_to_rotate]
            waypoint_dict_copy = move_waypoint(
                waypoint_dict_copy, converts_to, waypoint_dict[pos])
        return waypoint_dict_copy
    elif rotation_side == 'R':
        for pos in ['east', 'north']:
            starting_pos = ordered_positions.index(pos)
            index_after_rotation = starting_pos+postions_to_rotate
            if index_after_rotation >= len(ordered_positions):
                index_after_rotation = index_after_rotation - \
                    len(ordered_positions)
            converts_to = ordered_positions[index_after_rotation]
            waypoint_dict_copy = move_waypoint(
                waypoint_dict_copy, converts_to, waypoint_dict[pos])
        return waypoint_dict_copy


def parse_movement_with_waypoint(ship_instructions):
    waypoint_dict = defaultdict(int)
    waypoint_dict['north'] = 1
    waypoint_dict['east'] = 10
    movement_dict = defaultdict(int)
    movement_dict['north'] = 0
    movement_dict['east'] = 0

    for instruction in ship_instructions:
        if instruction[0] == 'N':
            waypoint_dict['north'] += int(instruction[1:])
        elif instruction[0] == 'S':
            waypoint_dict = move_south(waypoint_dict, int(instruction[1:]))
        elif instruction[0] == 'E':
            waypoint_dict['east'] += int(instruction[1:])
        elif instruction[0] == 'W':
            waypoint_dict = move_west(waypoint_dict, int(instruction[1:]))
        elif instruction[0] == 'F':
            movement_dict = move_forward_by_waypoint(
                movement_dict, waypoint_dict, int(instruction[1:]))
        elif instruction[0] == 'L' or instruction[0] == 'R':
            waypoint_dict = rotate_waypoint_around_ship(
                waypoint_dict, instruction[0], int(instruction[1:]))
    return movement_dict


def solve_part_one(ship_instructions):
    movement_dict = parse_movement(ship_instructions)
    return compute_manhattan_distance(movement_dict)


def solve_part_two(ship_instructions):
    movement_dict = parse_movement_with_waypoint(ship_instructions)
    return compute_manhattan_distance(movement_dict)


print('Part one. The distance moved by the ship is: {}.'.format(
    solve_part_one(ship_instructions)))
print('Part two. The distance moved by the ship is: {}.'.format(
    solve_part_two(ship_instructions)))
