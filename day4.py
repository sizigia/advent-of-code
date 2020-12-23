import re

with open('data/day4input.txt', 'r') as input_:
    pssprt_input = input_.read()


def generate_passport(pssprt_str):
    pairs = pssprt_str.split()
    passport = {}

    for pair in pairs:
        key, value = pair.split(':')
        passport[key] = value

    return passport


passport_list = []
p = ''
for i in pssprt_input.split('\n'):
    if i:
        p += i + ' '
    else:
        if p not in passport_list:
            passport_list.append(generate_passport(p.strip()))
            p = ''


def scan_fields(pssprt):
    req_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    pssprt_fields = pssprt.keys()

    return req_fields.issubset(pssprt_fields)


def count_valid_passports(pssprt_list):
    valid_pssprt = 0
    for p in range(len(passport_list)):
        if scan_fields(passport_list[p]):
            valid_pssprt += 1

    return valid_pssprt


def year_check(year, yrmin, yrmax): return year >= yrmin and year <= yrmax


def height_check(value):
    hgt = {
        'r': "(cm|in)",
        'cm': (150, 193),
        'in': (59, 76)
    }
    result = False
    match = re.split(hgt['r'], value)

    if len(match) > 1:
        p_hgt, p_unit, _ = match
        p_hgt = int(p_hgt)
        result = year_check(p_hgt, *hgt[p_unit])

    return result


def hair_color_pid_check(key, value):
    keys = {
        'hcl': "#([0-9]|[a-f]){6}",
        'pid': "\d{9}"}

    if key == "pid" and len(value) > 9:
        return False

    return bool(re.search(keys[key], value))


def eye_color_check(value):
    ecl = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')

    return value in ecl


answer_1 = count_valid_passports(passport_list)


def scan_values(passport):
    p_values = {}

    field_rules = {
        'byr': (1920, 2002),
        'iyr': (2010, 2020),
        'eyr': (2020, 2030)
    }

    for key in passport.keys():
        if key in ('byr', 'iyr', 'eyr'):
            p_values[key] = year_check(int(passport[key]), *field_rules[key])
        elif key == 'hgt':
            p_values[key] = height_check(passport[key])
        elif key in ('hcl', 'pid'):
            p_values[key] = hair_color_pid_check(key, passport[key])
        elif key == 'ecl':
            p_values[key] = eye_color_check(passport[key])

    return all(p_values.values())


def count_valid_fields_n_vals(pssprt_list):
    valid_pssprt = 0
    for p in range(len(pssprt_list)):
        if scan_fields(pssprt_list[p]) and scan_values(pssprt_list[p]):
            valid_pssprt += 1

    return valid_pssprt


answer_2 = count_valid_fields_n_vals(passport_list)

text_result = '\t--- PART ONE ---\nIf we treat "cid" as optional, the batch file has {} valid passports.\n\n\t--- PART TWO - --\nIf we count the number of valid passports - those that have al required fields and valid values, we have {} valid passports.\n'.format(
    answer_1, answer_2)
print(text_result)
