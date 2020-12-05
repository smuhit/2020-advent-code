data = open('input.txt').read().split()


seats = []
for datum in data:
    lower = 0
    upper = 127
    for x in range(7):
        if datum[x] == 'F':
            upper -= int((upper - lower)/ 2) + 1
        if datum[x] == 'B':
            lower += int((upper - lower)/ 2) + 1

    to_push = [lower]

    lower = 0
    upper = 7
    for x in range(3):
        if datum[x + 7] == 'L':
            upper -= int((upper - lower)/ 2) + 1
        if datum[x + 7] == 'R':
            lower += int((upper - lower)/ 2) + 1

    to_push.append(lower)
    seats.append(to_push)

# Part 1
ids = []
for seat in seats:
    row, col = seat
    ids.append(row * 8 + col)

print('Max Id', max(ids))

min_id = min(ids)
max_id = max(ids)

set_ids = set(ids)

for x in range(min_id, max_id + 1):
    if (x not in set_ids) and ((x + 1) in set_ids) and ((x - 1) in set_ids):
        break

print('Mine', x)