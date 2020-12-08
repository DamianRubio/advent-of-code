input_file = '2020/08/input.txt'

# Reading the input
raw_instructions = open(input_file).read().strip('\n').split('\n')


def execute_instructions(raw_instructions, return_value=True):
    executed_instructions = set()
    accumulator = 0
    executing_id = 0

    while executing_id < len(raw_instructions):
        if executing_id in executed_instructions:
            if return_value:
                return accumulator
            else:
                return None
        executed_instructions.add(executing_id)
        if raw_instructions[executing_id][:3] == 'nop':
            executing_id += 1
        elif raw_instructions[executing_id][:3] == 'acc':
            accumulator += int(raw_instructions[executing_id][3:])
            executing_id += 1
        elif raw_instructions[executing_id][:3] == 'jmp':
            executing_id += int(raw_instructions[executing_id][3:])
    return accumulator


def solve_part_one(raw_instructions):
    return execute_instructions(raw_instructions)


def solve_part_two(raw_instructions):
    for id in range(len(raw_instructions)):
        if raw_instructions[id][:3] == 'nop':
            new_list = raw_instructions.copy()
            new_list[id] = 'jmp ' + raw_instructions[id][3:]
            accumulator = execute_instructions(new_list, False)
            if accumulator:
                return accumulator
        elif raw_instructions[id][:3] == 'jmp':
            new_list = raw_instructions.copy()
            new_list[id] = 'nop ' + raw_instructions[id][3:]
            accumulator = execute_instructions(new_list, False)
            if accumulator:
                return accumulator
    return execute_instructions(new_list, False)


print("Part one. The value of the accumulator before any second execution is: {}.".format(
    solve_part_one(raw_instructions)))
print("Part two. The value of the accumulator after the change is: {}.".format(
    solve_part_two(raw_instructions)))
