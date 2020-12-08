from collections import Counter

input_file = '2020/06/input.txt'

# Parsing batches of answers of each group
batched_answers = open(input_file).read().split('\n\n')
batched_answers = [answer.split('\n') for answer in batched_answers]


def solve_part_one(batched_answers):
    return sum([len(set(''.join(answers))) for answers in batched_answers])


def solve_part_two(batched_answers):
    common_answers = 0
    for answers in batched_answers:
        n_persons = len(answers)
        joined_answers = ''.join(answers)
        character_counts = Counter(joined_answers)
        for _, count in character_counts.items():
            if count == n_persons:
                common_answers += 1
    return common_answers


print('Part one. The sum of those counts is: {}'.format(
    solve_part_one(batched_answers)))
print('Part two. The sum of those counts is: {}'.format(
    solve_part_two(batched_answers)))
