data = open('input.txt').read().split('\n')

part = 0
parsed_data = {
    'your ticket': [],
    'nearby tickets': []
}


for datum in data:
    if datum == '':
        part += 1
        continue
    if part == 0:
        key, val = datum.split(': ')
        parsed_data[key] = []
        val_ranges = val.split(' or ')
        for val_range in val_ranges:
            low, high = val_range.split('-')
            parsed_data[key].append((int(low), int(high)))
    elif part == 1:
        if not datum.startswith('your ticket'):
            parsed_data['your ticket'] += [int(x) for x in datum.split(',')]
    elif part == 2:
        if not datum.startswith('nearby tickets'):
            parsed_data['nearby tickets'] += [int(x) for x in datum.split(',')]

# Part 1
invalid_tickets = []
for ticket in parsed_data['nearby tickets']:
    for key in parsed_data.keys() - {'your ticket', 'nearby tickets'}:
        valid = False
        for low, high in parsed_data[key]:
            if ticket >= low and ticket <= high:
                valid = True
                break
        if valid:
            break
    if not valid:
        invalid_tickets.append(ticket)
print('Error Rate', sum(invalid_tickets))

# Part 2
invalid_tickets = set(invalid_tickets)
num_fields = len(parsed_data['your ticket'])
fields = list(parsed_data.keys() - {'your ticket', 'nearby tickets'})
field_arbiter = [set(x) for x in [fields] * num_fields]
ticket_lines = []
for x in range(0, len(parsed_data['nearby tickets']), num_fields):
    ticket_lines.append(parsed_data['nearby tickets'][x:x+num_fields])
ticket_lines = [line for line in ticket_lines if set(line) - invalid_tickets == set(line)]

tickets_to_check = ticket_lines.copy()
tickets_to_check.insert(0, parsed_data['your ticket'])

to_remove = {k: set() for k in range(num_fields)}
for idx, potential_fields in enumerate(field_arbiter):
    for ticket_line in tickets_to_check:
        for field in potential_fields:
            remove = True
            for low, high in parsed_data[field]:
                if ticket_line[idx] >= low and ticket_line[idx] <= high:
                    remove = False
                    break
            if remove:
                to_remove[idx].add(field)

for idx in to_remove:
    for field in to_remove[idx]:
        field_arbiter[idx].remove(field)

field_checker = set(fields)
while True:
    to_remove = []
    for idx, val_set in enumerate(field_arbiter):
        if len(val_set) == 1 and val_set.issubset(field_checker):
            val = list(val_set)[0]
            to_remove.append((idx, val))
            field_checker.remove(val)
    if not to_remove:
        break
    for x, val in to_remove:
        for idx, val_set in enumerate(field_arbiter):
            if val in val_set and idx != x:
                val_set.remove(val)

if any(len(x) != 1 for x in field_arbiter):
    print('Something is wrong')
    exit(1)
field_arbiter = [list(x)[0] for x in field_arbiter]

prod = 1
for idx, ticket_val in enumerate(parsed_data['your ticket']):
    if field_arbiter[idx].startswith('departure'):
        prod *= ticket_val

print('Prod', prod)