from collections import defaultdict

input_file = '2020/15/input.txt'

numbers = [int(n) for n in open(input_file).readline().split(',')]

def play_memory_game(numbers, n_turns):
    ages = defaultdict(int)

    for pos, number in enumerate(numbers[:len(numbers)-1]):
        ages[number] = pos+1

    current_number = numbers[-1]
    for i in range(len(numbers), n_turns):
        if current_number in ages:
            turn_difference = i - ages[current_number]
            ages[current_number] = i
            current_number = turn_difference
        else:
            ages[current_number] = i
            current_number = 0
    return current_number

print('Part one. The 2020th number spoken will be: {}.'.format(
    play_memory_game(numbers, 2020)))
print('Part two. The 30000000th number spoken will be: {}.'.format(
    play_memory_game(numbers, 30000000)))
