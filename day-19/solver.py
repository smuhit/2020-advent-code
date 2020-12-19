import re

data = open('input.txt').read().split('\n')

rules = {}

for r_idx, datum in enumerate(data):
    if datum == '':
        break
    key, value = datum.split(': ')
    if '"' in value:
        value = value.split('"')[1]
        rules[int(key)] = value
    else:
        key_rules = []
        for key_rule in value.split(' | '):
            key_rules.append([int(x) for x in key_rule.split()])
        rules[int(key)] = key_rules

messages = [data[m_idx] for m_idx in range(r_idx, len(data)) if data[m_idx] != '']

def construct(idx):
    if isinstance(rules[idx], str):
        return rules[idx]
    constructor = '(' if len(rules[idx]) > 1 else ''
    for key_rule_part in rules[idx]:
        constructor += '|' if len(rules[idx]) > 1 and constructor != '(' else ''
        for key_rule_unit in key_rule_part:
            constructor += construct(key_rule_unit)
    constructor += ')' if len(rules[idx]) > 1 else ''
    return constructor

# Part 1

matcher = '^'

matcher += construct(0)
matcher += '$'

matching = []
for message in messages:
    if re.match(matcher, message):
        matching.append(message)

print('Count of 0:', len(matching))

# Part 2

def construct(idx):
    # Handling special cases 8 and 11 separetly
    if idx == 8:  # 42 | 42 8
        return f'({construct(42)})+'
    if idx == 11:  # 42 31 | 42 11 31
        max_length = len(max(messages, key = len)) // 2 # Can't repeat more than this...
        constructor_42 = construct(42)
        constructor_31 = construct(31)
        constructors = []
        for i in range(1, max_length):
            constructors.append(f'{constructor_42}{{{i}}}{constructor_31}{{{i}}}')

        constructor = f'({"|".join(constructors)})'
        return constructor

    if isinstance(rules[idx], str):
        return rules[idx]
    constructor = '(' if len(rules[idx]) > 1 else ''
    for key_rule_part in rules[idx]:
        constructor += '|' if len(rules[idx]) > 1 and constructor != '(' else ''
        for key_rule_unit in key_rule_part:
            constructor += construct(key_rule_unit)
    constructor += ')' if len(rules[idx]) > 1 else ''
    return constructor


matcher = '^'

matcher += construct(0)
matcher += '$'

matching = []
for message in messages:
    if re.match(matcher, message):
        matching.append(message)

print('Count of 0:', len(matching))
