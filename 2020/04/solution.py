import re
from collections import defaultdict

input_file = '2020/04/input.txt'

passports = []

# Parsing batches to have a dict representing each of the passports
batched_passports = open(input_file).read().split('\n\n')
batched_passports = [' '.join(i.split('\n')) for i in batched_passports]
batched_passports = [i.split(' ') for i in batched_passports]

passports = []
for passport in batched_passports:
    passport_info = defaultdict(str)
    for term in passport:
        passport_info[term[0:3]] = term[4:]
    passports.append(passport_info)


class Passport(object):

    def __init__(self, byr=None, iyr=None, eyr=None, hgt=None, hcl=None, ecl=None, pid=None, cid=None):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid

    def is_valid(self):
        # A passport is invalid if it is missing any of its fields but the 'cid'.
        return self.byr and self.iyr and self.eyr and self.hgt and self.hcl and self.ecl and self.pid

    def is_valid_byr(self):
        if self.byr:
            return re.match(r'^[0-9]{4}$', self.byr) and int(self.byr) >= 1920 and int(self.byr) <= 2002
        return False

    def is_valid_iyr(self):
        if self.iyr:
            return re.match(r'^[0-9]{4}$', self.iyr) and int(self.iyr) >= 2010 and int(self.iyr) <= 2020
        return False

    def is_valid_eyr(self):
        if self.eyr:
            return re.match(r'^[0-9]{4}$', self.eyr) and int(self.eyr) >= 2020 and int(self.eyr) <= 2030
        return False

    def is_valid_hgt(self):
        if self.hgt:
            if re.search(r'cm', self.hgt) and re.match(r'([0-9]{3})(cm)', self.hgt):
                matched = re.match(r'([0-9]{3})(cm)', self.hgt)
                if int(matched.group(1)) >= 150 and int(matched.group(1)) <= 193:
                    return True
            elif re.search(r'in', self.hgt) and re.match(r'([0-9]{2})in', self.hgt):
                matched = re.match(r'([0-9]{2})in', self.hgt)
                if int(matched.group(1)) >= 59 or int(matched.group(1)) <= 76:
                    return True
        return False

    def is_valid_hcl(self):
        if self.hcl:
            return re.match(r'^#[a-f0-9]{6}$', self.hcl)
        return False

    def is_valid_ecl(self):
        if self.ecl:
            return self.ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        return False

    def is_valid_pid(self):
        if self.pid:
            return re.match(r'^[0-9]{9}$', self.pid)
        return False

    def is_valid_considering_data(self):
        return self.is_valid_byr() and self.is_valid_iyr() and self.is_valid_eyr() and self.is_valid_hgt() and self.is_valid_hcl() and self.is_valid_ecl() and self.is_valid_pid()


def solve_part_one(passports):
    valid_passports = 0
    for passport in passports:
        passport_object = Passport(**passport)
        if passport_object.is_valid():
            valid_passports += 1
    return valid_passports


def solve_part_two(passports):
    valid_passports = 0
    for passport in passports:
        passport_object = Passport(**passport)
        if passport_object.is_valid_considering_data():
            valid_passports += 1
    return valid_passports


print('The number of passports parsed is: {}'.format(len(passports)))
print('Part one. The number of valid passports is: {}.'.format(
    solve_part_one(passports)))
print('Part two. The number of valid passports is: {}.'.format(
    solve_part_two(passports)))
