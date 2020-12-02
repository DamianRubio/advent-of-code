input_file = '2020/02/input.txt'

with open(input_file) as f:
    pwd_and_policies = [i.split(" ") for i in f.read().splitlines()]


def solve_part_one(pwd_and_policies):
    valid_passwords = 0
    for pwd_and_policy in pwd_and_policies:
        min_appearances = int(pwd_and_policy[0].split('-')[0])
        max_appearances = int(pwd_and_policy[0].split('-')[1])
        letter = pwd_and_policy[1][0]
        password = pwd_and_policy[2]
        if password.count(letter) >= min_appearances and password.count(letter) <= max_appearances:
            valid_passwords += 1
    return valid_passwords


def solve_part_two(pwd_and_policies):
    valid_passwords = 0
    for pwd_and_policy in pwd_and_policies:
        pos_one = int(pwd_and_policy[0].split('-')[0])
        pos_two = int(pwd_and_policy[0].split('-')[1])
        letter = pwd_and_policy[1][0]
        password = pwd_and_policy[2]
        if (password[pos_one-1] == letter) is not (password[pos_two-1] == letter):
            valid_passwords += 1
    return valid_passwords


print("Part one. The number of valid passwords is: {}.".format(
    solve_part_one(pwd_and_policies)))
print("Part two. The number of valid passwords is: {}.".format(
    solve_part_two(pwd_and_policies)))
