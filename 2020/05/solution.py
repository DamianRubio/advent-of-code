input_file = '2020/05/input.txt'

with open(input_file) as f:
    boarding_passes = [i for i in f.read().splitlines()]


def check_binary_space(binary_space_str, lower, upper, lower_sym='F', upper_sym='B'):
    if len(binary_space_str) == 1:
        if binary_space_str[0] == lower_sym:
            return lower
        elif binary_space_str[0] == upper_sym:
            return upper
    else:
        if binary_space_str[0] == lower_sym:
            upper = upper - round((upper-lower)/2)
            return check_binary_space(binary_space_str[1:], lower, upper, lower_sym, upper_sym)
        elif binary_space_str[0] == upper_sym:
            lower = lower + round((upper-lower)/2)
            return check_binary_space(binary_space_str[1:], lower, upper, lower_sym, upper_sym)


def convert_binary_to_seat(boarding_passes):
    seats = []
    for boarding_code in boarding_passes:
        row = check_binary_space(boarding_code[:7], 0, 127)
        column = check_binary_space(boarding_code[7:], 0, 7, 'L', 'R')
        seats.append((row, column))
    return seats


def convert_seat_to_seat_id(tuple_seat):
    row, column = tuple_seat
    return row*8+column


def solve_part_one(boarding_passes):
    seat_ids = [convert_seat_to_seat_id(
        tuple_seat) for tuple_seat in convert_binary_to_seat(boarding_passes)]
    return max(seat_ids)


def solve_part_two(boarding_passes):
    seats = convert_binary_to_seat(boarding_passes)
    seats.sort(key=lambda tup: (tup[0], tup[1]))

    for i in range(seats[0][0], seats[-1][0]+1):
        for j in range(8):
            if (i, j) not in seats:
                return convert_seat_to_seat_id((i, j))

    return "No empty seat found"


print('Part one. The highest seat ID is: {}'.format(
    solve_part_one(boarding_passes)))
print('Part two. Your seat ID is: {}'.format(solve_part_two(boarding_passes)))
