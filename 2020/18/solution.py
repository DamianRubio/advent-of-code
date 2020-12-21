import re

input_file = '2020/18/input.txt'

operations = [line.strip() for line in open(input_file).readlines()]
brackets_regex = r'(\([^()]+\))'


def solve_left_right(operations):
    operations = operations.split(' ')
    current_result = int(operations[0])
    while operations:
        operation_to_perform = operations.pop(0)
        if operation_to_perform == '+':
            current_result += int(operations.pop(0))
        elif operation_to_perform == '*':
            current_result *= int(operations.pop(0))
    return current_result


def solve_add_first(operations):
    if ('+' in operations and not '*' in operations) or ('*' in operations and not '+' in operations):
        return solve_left_right(operations)

    operations = operations.split(' ')
    for pos, char in enumerate(operations):
        if char == '+':
            result = int(operations[pos-1]) + int(operations[pos+1])
            for i in range(0, 3):
                del operations[pos-1]
            operations.insert(pos-1, str(result))
            break
    return solve_add_first(' '.join(operations))


def solve_operations(operations, precedence=solve_left_right):
    if re.search(brackets_regex, operations):
        bracket_operation = re.search(brackets_regex, operations).group()
        result_bracket = precedence(
            bracket_operation[1:len(bracket_operation)-1])
        operations = operations.replace(bracket_operation, str(result_bracket))
        return solve_operations(operations, precedence)
    else:
        return precedence(operations)


def solve_part_one(operations):
    results = []
    for operations_line in operations:
        results.append(solve_operations(operations_line))
    return sum(results)


def solve_part_two(operations):
    results = []
    for operations_line in operations:
        results.append(solve_operations(
            operations_line, precedence=solve_add_first))
    return sum(results)


print('Part one. The sum of the resulting values is: {}.'.format(
    solve_part_one(operations)))
print('Part two. The sum of the resulting values is: {}.'.format(
    solve_part_two(operations)))
