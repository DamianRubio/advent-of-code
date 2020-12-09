from itertools import combinations

input_file = '2020/09/input.txt'

numbers = [int(n) for n in open(input_file).readlines()]


def solve_part_one(numbers, preamble_length=25):
    current_id = preamble_length
    while current_id < len(numbers):
        all_possible_sums = set([sum(t) for t in combinations(
            numbers[current_id-preamble_length:current_id], 2)])
        if numbers[current_id] in all_possible_sums:
            current_id += 1
        else:
            return numbers[current_id]
    return None


def find_contiguous_sum(numbers, num_to_find):
    left_id = 0
    right_id = 1

    while right_id <= len(numbers):
        if sum(numbers[left_id:right_id]) < num_to_find:
            right_id += 1
        elif sum(numbers[left_id:right_id]) > num_to_find:
            left_id += 1
        elif sum(numbers[left_id:right_id]) == num_to_find:
            return numbers[left_id:right_id]
        if left_id == right_id:
            right_id += 1
    return None


def solve_part_two(numbers, preamble_length=25):
    num_to_find = solve_part_one(numbers, preamble_length)
    valid_contiguous_numbers = find_contiguous_sum(numbers, num_to_find)
    return max(valid_contiguous_numbers) + min(valid_contiguous_numbers)


print('Part one. The first that does not meet the property is: {}.'.format(
    solve_part_one(numbers)))
print('Part two. The encryption weakness is: {}.'.format(
    solve_part_two(numbers)))
