from copy import deepcopy

data = open('input.txt').read().split()

# Part 1

def seat_shift(seats):
    changed = False
    seat_copy = deepcopy(seats)
    for x, row in enumerate(seat_copy):
        for y, val in enumerate(row):
            if val == '.':
                continue
            occupied = 0
            adjacents = (
                (x-1, y-1), (x-1, y), (x-1, y+1),
                (x,   y-1),           (x,   y+1),
                (x+1, y-1), (x+1, y), (x+1, y+1)
            )
            for adj_x, adj_y in adjacents:
                if adj_x < 0 or adj_y < 0:
                    continue
                try:
                    if seat_copy[adj_x][adj_y] == '#':
                        occupied += 1
                except IndexError:
                    continue
            if val == 'L' and occupied == 0:
                changed = True
                seats[x][y] = '#'
            elif val == '#' and occupied >= 4:
                changed = True
                seats[x][y] = 'L'
    return changed

data_copy = [list(row) for row in data]

while seat_shift(data_copy):
    continue

print('occupied', sum(x.count('#') for x in data_copy))


# Part 2: Copying func from part 1 and modifying...

def seat_shift(seats):
    changed = False
    seat_copy = deepcopy(seats)
    for x, row in enumerate(seat_copy):
        for y, val in enumerate(row):
            if val == '.':
                continue
            occupied = 0
            directions = (
                (-1, -1), (-1, 0), (-1, +1),
                ( 0, -1),          ( 0, +1),
                (+1, -1), (+1, 0), (+1, +1)
            )
            for dir_x, dir_y in directions:
                adj_x = x + dir_x
                adj_y = y + dir_y
                while True:
                    if adj_x < 0 or adj_y < 0:
                        break
                    try:
                        if seat_copy[adj_x][adj_y] == '#':
                            occupied += 1
                            break
                        elif seat_copy[adj_x][adj_y] == 'L':
                            break
                        adj_x += dir_x
                        adj_y += dir_y
                    except IndexError:
                        break
            if val == 'L' and occupied == 0:
                changed = True
                seats[x][y] = '#'
            elif val == '#' and occupied >= 5:
                changed = True
                seats[x][y] = 'L'
    return changed

data_copy = [list(row) for row in data]

while seat_shift(data_copy):
    continue

print('occupied', sum(x.count('#') for x in data_copy))
