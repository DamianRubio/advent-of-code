from collections import defaultdict
from copy import deepcopy
import re

input_file = '2020/14/input.txt'
program = [line.strip() for line in open(input_file).readlines()]


def is_mask(instruction):
    return instruction[:4] == 'mask'


def get_memory_pos(instruction):
    regex = r'\[([0-9]+)\]'
    match = re.search(regex, instruction)
    return int(match.group(1))


def apply_mask(value, mask):
    value_binary = format(value, '036b')
    value_binary_masked = [n for n in value_binary]
    for pos, value in enumerate(mask):
        if value != 'X':
            value_binary_masked[pos] = value
    return int(''.join(value_binary_masked), 2)


def get_all_memory_pos(memory_pos, mask):
    memory_pos = format(memory_pos, '036b')
    memory_pos_list = [n for n in memory_pos]
    all_memory_pos = [memory_pos_list]

    for pos, value in enumerate(mask):
        if value == '1':
            for address in all_memory_pos:
                address[pos] = '1'
        elif value == 'X':
            iterations = len(all_memory_pos)
            for i in range(iterations):
                original_address = all_memory_pos.pop(0)
                original_address_zero = deepcopy(original_address)
                original_address_one = deepcopy(original_address)
                original_address_zero[pos] = '0'
                all_memory_pos.append(original_address_zero)
                original_address_one[pos] = '1'
                all_memory_pos.append(original_address_one)
    return [int(''.join(address_list), 2) for address_list in all_memory_pos]


def solve_part_one(instructions):
    current_mask = ''
    memory = defaultdict(int)

    for instruction in instructions:
        if is_mask(instruction):
            current_mask = instruction[7:]
        else:
            memory_pos = get_memory_pos(instruction)
            value = int(instruction.split(' = ')[1])
            memory[memory_pos] = apply_mask(value, current_mask)
    return sum(memory.values())


def solve_part_two(instructions):
    current_mask = ''
    memory = defaultdict(int)

    for instruction in instructions:
        if is_mask(instruction):
            current_mask = instruction[7:]
        else:
            memory_pos = get_memory_pos(instruction)
            all_memory_pos = get_all_memory_pos(memory_pos, current_mask)
            value = int(instruction.split(' = ')[1])
            for address in all_memory_pos:
                memory[address] = value
    return sum(memory.values())


print('Part one. The sum of the values in the memory is: {}.'.format(
    solve_part_one(program)))
print('Part two. The sum of the values in the memory is: {}.'.format(
    solve_part_two(program)))
