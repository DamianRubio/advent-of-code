from collections import defaultdict

input_file = '2020/01/input.txt'

with open(input_file) as f:
    expenses = [int(i) for i in f.read().splitlines()]


def solve_part_one(expenses):
    # First part solution
    mapper = defaultdict(int)

    for position, expense in enumerate(expenses):
        aim = 2020 - expense
        if mapper[aim]:
            return "First part solution is: {}".format(aim*expense)
        else:
            mapper[expense] = position
    return "No solution found :("


def solve_part_two(expenses):
    # Second part solution
    mapper = defaultdict(list)

    for position, expense in enumerate(expenses):
        aim = 2020 - expense
        for inside_pos, inside_expense in enumerate(expenses[:position] + expenses[(position + 1):]):
            aim = 2020 - expense - inside_expense
            if mapper[aim]:
                return "Second part solution is: {}".format(aim*expense*inside_expense)
            else:
                mapper[inside_expense] = position
        mapper = defaultdict(list)
    return "No solution found :("


print(solve_part_one(expenses))
print(solve_part_two(expenses))
