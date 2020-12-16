from math import ceil
from itertools import count

input_file = '2020/13/input.txt'

problem_input = open(input_file)

earliest_timestamp = int(problem_input.readline())
bus_ids = problem_input.readline().split(',')


def get_valid_ids(bus_ids):
    valid_ids = [int(bus_id) for bus_id in bus_ids if bus_id != 'x']
    valid_ids.sort()
    return valid_ids


def get_earliest_departure(earliest_timestamp, valid_ids):
    closest_timestamp_to_departure = []
    for bus_id in valid_ids:
        if earliest_timestamp % bus_id == 0:
            return bus_id, earliest_timestamp
        else:
            closest_timestamp_to_departure.append(
                bus_id*ceil(earliest_timestamp/bus_id))
    return min(closest_timestamp_to_departure), valid_ids[closest_timestamp_to_departure.index(min(closest_timestamp_to_departure))]


def solve_part_one(earliest_timestamp, bus_ids):
    valid_ids = get_valid_ids(bus_ids)
    departure_time, bus_id = get_earliest_departure(
        earliest_timestamp, valid_ids)
    return (departure_time-earliest_timestamp)*bus_id


def solve_part_two(bus_ids):
    minute_differences = [bus_ids.index(i) for i in bus_ids if i != 'x']
    clean_bus_ids = [int(i) for i in bus_ids if i != 'x']

    time = 0
    step = 1
    for bus_time, time_difference in zip(clean_bus_ids, minute_differences):
        for x_steps_time in count(time, step):
            if (x_steps_time + time_difference) % bus_time == 0:
                time = x_steps_time
                step = step * bus_time
                break
    return time

print('Part one. The ID of the earliest bus multiplied by the number of minutes to wait is: {}.'.format(
    solve_part_one(earliest_timestamp, bus_ids)))
print('Part one. The earliest timestamp such all the bus IDs depart at offsets matches is: {}.'.format(
    solve_part_two(bus_ids)))
