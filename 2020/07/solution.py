from collections import defaultdict

input_file = '2020/07/input.txt'

with open(input_file) as f:
    raw_rules = [i for i in f.read().splitlines()]


def convert_rules_to_dicts(raw_rules):
    rule_colors = defaultdict(list)
    rule_amounts = defaultdict(list)

    for rule in raw_rules:
        splitted_rule = rule.split(' ')
        main_color = ' '.join(splitted_rule[:2])
        for pos, word in enumerate(splitted_rule):
            if word.isdigit():
                amount = int(word)
                color = ' '.join(splitted_rule[pos+1:pos+3])
                rule_colors[color].append(main_color)
                rule_amounts[color].append(amount)

    return rule_colors, rule_amounts


def convert_rules_to_reverse_dicts(raw_rules):
    rule_colors = defaultdict(list)
    rule_amounts = defaultdict(list)

    for rule in raw_rules:
        splitted_rule = rule.split(' ')
        main_color = ' '.join(splitted_rule[:2])
        for pos, word in enumerate(splitted_rule):
            if word.isdigit():
                amount = int(word)
                color = ' '.join(splitted_rule[pos+1:pos+3])
                rule_colors[main_color].append(color)
                rule_amounts[main_color].append(amount)

    return rule_colors, rule_amounts


def recursive_check_bag_rules_colors(bag_color, visited, rule_colors):
    for element in rule_colors[bag_color]:
        if element not in visited:
            visited.append(element)
            recursive_check_bag_rules_colors(element, visited, rule_colors)
    return visited


def recursive_check_bag_rules_amounts(bag_color, current_amount, rule_colors, rule_amounts):
    if not rule_colors[bag_color]:
        return 1
    else:
        for color, amount in zip(rule_colors[bag_color], rule_amounts[bag_color]):
            current_amount += amount * \
                recursive_check_bag_rules_amounts(
                    color, 1, rule_colors, rule_amounts)
    return current_amount


def solve_part_one(raw_rules):
    rule_colors, _ = convert_rules_to_dicts(raw_rules)
    original_color = 'shiny gold'
    which_contain_the_color = recursive_check_bag_rules_colors(
        original_color, [original_color], rule_colors)
    return len(which_contain_the_color)-1


def solve_part_two(raw_rules):
    rule_colors, rule_amounts = convert_rules_to_reverse_dicts(raw_rules)
    original_color = 'shiny gold'
    amount = recursive_check_bag_rules_amounts(
        original_color, 1, rule_colors, rule_amounts)
    return amount-1


aux, _ = convert_rules_to_reverse_dicts(raw_rules)
print(aux['shiny gold'])
print('Part one. The number of bag colors that can contain at least a shinny gold bag is: {}'.format(
    solve_part_one(raw_rules)))
print('Part two. The amount of bags you have to carry inside a shinny gold bag is: {}'.format(
    solve_part_two(raw_rules)))
