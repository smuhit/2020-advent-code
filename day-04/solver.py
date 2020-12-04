data = open('input.txt').read().split('\n')

passports = []
passport = {}
for line in data:
    if line == '':
        passports.append(passport)
        passport = {}
    parts = line.split()
    for part in parts:
        key, value = part.split(':')
        passport[key] = value

# Part 1
required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

valid_passports = []
for passport in passports:
    found = True
    for key in required:
        if key not in passport.keys():
            found = False
            break
    if found:
        valid_passports.append(passport)

print('Valid', len(valid_passports))


# Part 2
def all_in(a, b):
    for elem in a:
        if elem not in b:
            return False
    return True

def height(a):
    measure = a[-2:]
    value = a[:-2]
    if measure == 'cm':
        return int(value) >= 150 and int(value) <= 193
    if measure == 'in':
        return int(value) >= 59 and int(value) <= 76
    return False

rules = {
    0: lambda x: int(x) >= 1920 and int(x) <= 2002,
    1: lambda x: int(x) >= 2010 and int(x) <= 2020,
    2: lambda x: int(x) >= 2020 and int(x) <= 2030,
    3: lambda x: height(x),
    4: lambda x: len(x) == 7 and x[0] == '#' and all_in(x[1:], '0123456789abcdef'),
    5: lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
    6: lambda x: len(x) == 9 and all_in(x, '0123456789'),
}

valid = 0
for passport in valid_passports:
    found = True
    for idx, key in enumerate(required):
        if  not rules[idx](passport[key]):
            found = False
            break
    if found:
        valid += 1

print('Valid', valid)
