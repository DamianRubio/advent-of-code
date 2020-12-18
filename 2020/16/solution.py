from collections import defaultdict
from functools import reduce

input_file = '2020/16/input.txt'


def parse_input(file_name):
    valid_rules = defaultdict(list)
    all_tickets = []
    with open(file_name) as f:
        for line in f:
            if '-' in line:
                splitted_rule = line.split(':')
                rule_name = splitted_rule[0]
                ranges = splitted_rule[1].split(' or ')
                ranges_list = [n for n in range(
                    int(ranges[0].split('-')[0]), int(ranges[0].split('-')[1])+1)]
                ranges_list += [n for n in range(
                    int(ranges[1].split('-')[0]), int(ranges[1].split('-')[1])+1)]
                valid_rules[rule_name] = ranges_list
            if line.split(',')[0].isnumeric():
                all_tickets.append([int(n) for n in line.split(',')])
    return valid_rules, all_tickets


def solve_part_one(input_file):
    valid_rules, all_tickets = parse_input(input_file)
    wrong_values = 0

    all_possible_numbers = set(x for l in valid_rules.values() for x in l)
    for ticket in all_tickets:
        for value in ticket:
            if value not in all_possible_numbers:
                wrong_values += value

    return wrong_values


def get_all_valid_tickets(valid_rules, all_tickets):
    valid_tickets = []

    all_possible_numbers = set(x for l in valid_rules.values() for x in l)
    for ticket in all_tickets:
        valid = True
        for value in ticket:
            if value not in all_possible_numbers:
                valid = False
        if valid:
            valid_tickets.append(ticket)
    return valid_tickets


def prune_dict(possible_fields, final_dict):
    if not possible_fields:
        return final_dict
    value_to_clean = None
    for k, v in possible_fields.items():
        if len(v) == 1:
            value_to_clean = v[0]
            final_dict[k] = value_to_clean
            break
    if value_to_clean:
        for k, v in possible_fields.items():
            if value_to_clean in v:
                possible_fields[k].remove(value_to_clean)
    possible_fields = {k: v for k, v in possible_fields.items() if v}
    return prune_dict(possible_fields, final_dict)


def solve_part_two(input_file):
    valid_rules, all_tickets = parse_input(input_file)
    valid_tickets = get_all_valid_tickets(valid_rules, all_tickets)

    possible_fields = defaultdict(list)
    for pos in range(len(valid_tickets[0])):
        possible_fields[pos] = list(valid_rules.keys())

    for ticket in valid_tickets:
        for pos, value in enumerate(ticket):
            pos_fields = possible_fields.get(pos)
            for field in possible_fields[pos]:
                if value not in valid_rules[field]:
                    pos_fields.remove(field)
            possible_fields[pos] = pos_fields

    final_dict = prune_dict(possible_fields, defaultdict(str))
    valid_positions = [k for k, v in final_dict.items() if 'departure' in v]
    my_ticket_values = []
    for valid_pos in valid_positions:
        my_ticket_values.append(all_tickets[0][valid_pos])
    return reduce(lambda x, y: x*y, my_ticket_values)


print('Part one. The ticket scanning error rate is: {}'.format(
    solve_part_one(input_file)))
print('Part two. If you multiply the six values together you get: {}'.format(
    solve_part_two(input_file)))
