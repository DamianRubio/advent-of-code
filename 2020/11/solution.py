import copy

input_file = '2020/11/input.txt'

OCCUPIED_SEAT = '#'
EMPTY_SEAT = 'L'
NO_SEAT = '.'

seat_rows = open(input_file).read().splitlines()
seat_map = [list(row) for row in seat_rows]


class RoomMapper():

    def __init__(self, seat_map):
        self.seat_map = seat_map

    def check_if_seat(self, i, j):
        return self.seat_map[i][j] != NO_SEAT

    def check_if_empty(self, i, j):
        return self.seat_map[i][j] == EMPTY_SEAT

    def check_if_occupied(self, i, j):
        return self.seat_map[i][j] == OCCUPIED_SEAT

    def get_adjacent_seats_status(self, i, j):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0,  -1),
                      (0,  1), (1,  -1), (1,  0), (1, 1)]
        min_i, max_i = 0, len(self.seat_map)-1
        min_j, max_j = 0, len(self.seat_map[0])-1
        result = []

        for (direction_i, direction_j) in directions:
            new_pos_i, new_pos_j = (direction_i+i, direction_j+j)
            if (new_pos_i >= min_i and new_pos_i <= max_i) and (new_pos_j >= min_j and new_pos_j <= max_j):
                result.append(self.seat_map[new_pos_i][new_pos_j])

        return result

    def count_occupied_seats(self):
        occupied_seats = 0
        for i in range(len(self.seat_map)):
            for j in range(len(self.seat_map[0])):
                if self.check_if_occupied(i, j):
                    occupied_seats += 1
        return occupied_seats

    def iterate(self):
        seat_map_copy = copy.deepcopy(self.seat_map)
        changed_in_iteration = False
        for i in range(len(self.seat_map)):
            for j in range(len(self.seat_map[0])):
                if self.check_if_empty(i, j):
                    adjacent_status = self.get_adjacent_seats_status(i, j)
                    if not OCCUPIED_SEAT in adjacent_status:
                        seat_map_copy[i][j] = OCCUPIED_SEAT
                        changed_in_iteration = True
                elif self.check_if_occupied(i, j):
                    adjacent_status = self.get_adjacent_seats_status(i, j)
                    if adjacent_status.count(OCCUPIED_SEAT) >= 4:
                        seat_map_copy[i][j] = EMPTY_SEAT
                        changed_in_iteration = True
        if changed_in_iteration:
            self.seat_map = seat_map_copy

        return changed_in_iteration

    def get_adjacent_seats_status_by_visibility(self, i, j):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0,  -1),
                      (0,  1), (1,  -1), (1,  0), (1, 1)]
        min_i, max_i = 0, len(self.seat_map)-1
        min_j, max_j = 0, len(self.seat_map[0])-1
        result = []

        for (direction_i, direction_j) in directions:
            new_pos_i, new_pos_j = (direction_i+i, direction_j+j)
            while (new_pos_i >= min_i and new_pos_i <= max_i) and (new_pos_j >= min_j and new_pos_j <= max_j):
                if not self.check_if_seat(new_pos_i, new_pos_j):
                    new_pos_i, new_pos_j = (
                        direction_i+new_pos_i, direction_j+new_pos_j)
                else:
                    result.append(self.seat_map[new_pos_i][new_pos_j])
                    break

        return result

    def iterate_by_visibility(self):
        seat_map_copy = copy.deepcopy(self.seat_map)
        changed_in_iteration = False
        for i in range(len(self.seat_map)):
            for j in range(len(self.seat_map[0])):
                if self.check_if_empty(i, j):
                    adjacent_status = self.get_adjacent_seats_status_by_visibility(
                        i, j)
                    if not OCCUPIED_SEAT in adjacent_status:
                        seat_map_copy[i][j] = OCCUPIED_SEAT
                        changed_in_iteration = True
                elif self.check_if_occupied(i, j):
                    adjacent_status = self.get_adjacent_seats_status_by_visibility(
                        i, j)
                    if adjacent_status.count(OCCUPIED_SEAT) >= 5:
                        seat_map_copy[i][j] = EMPTY_SEAT
                        changed_in_iteration = True
        if changed_in_iteration:
            self.seat_map = seat_map_copy

        return changed_in_iteration


def solve_part_one(seat_map):
    room_mapper = RoomMapper(seat_map)
    changed = room_mapper.iterate()
    while(changed):
        changed = room_mapper.iterate()
    return room_mapper.count_occupied_seats()


def solve_part_two(seat_map):
    room_mapper = RoomMapper(seat_map)
    changed = room_mapper.iterate_by_visibility()
    while(changed):
        changed = room_mapper.iterate_by_visibility()
    return room_mapper.count_occupied_seats()


print('Part one. The number of occupied seats after stabilization is: {}.'.format(
    solve_part_one(seat_map)))
print('Part two. The number of occupied seats after stabilization is: {}.'.format(
    solve_part_two(seat_map)))
