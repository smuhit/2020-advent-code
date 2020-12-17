data = open('input.txt').read().split('\n')

# Part 1

active_cubes = set()

for y, row in enumerate(data):
    for x, char in enumerate(row):
        if char == '#':
            active_cubes.add((x, y, 0))

def active_surrounding(active, x, y, z):
    count = 0
    for x1 in range(x - 1, x + 2):
        for y1 in range(y - 1, y + 2):
            for z1 in range(z - 1, z + 2):
                if (x, y, z) == (x1, y1, z1):
                    continue
                if (x1, y1, z1) in active:
                    count += 1
    return count


def cycle(active):
    new_active = active.copy()
    min_x = min([coord[0] for coord in new_active])
    max_x = max([coord[0] for coord in new_active])
    min_y = min([coord[1] for coord in new_active])
    max_y = max([coord[1] for coord in new_active])    
    min_z = min([coord[2] for coord in new_active])
    max_z = max([coord[2] for coord in new_active])
    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            for z in range(min_z - 1, max_z + 2):
                num_around = active_surrounding(active, x, y, z)
                if (x, y, z) in active and num_around not in (2, 3):
                    new_active.remove((x, y, z))
                if (x, y, z) not in active and num_around == 3:
                    new_active.add((x, y, z))
    return new_active

def cycle_count(active, count):
    new_active = active.copy()
    for _ in range(count):
        new_active = cycle(new_active)
    return new_active

print('6 cycles', len(cycle_count(active_cubes, 6)))

# Part 2 --- too lazy to refactor, copy + paste plus edit

active_cubes = set()

for x, row in enumerate(data):
    for w, char in enumerate(row):
        if char == '#':
            active_cubes.add((w, x, 0, 0))

def active_surrounding(active, w, x, y, z):
    count = 0
    for w1 in range(w - 1, w + 2):
        for x1 in range(x - 1, x + 2):
            for y1 in range(y - 1, y + 2):
                for z1 in range(z - 1, z + 2):
                    if (w, x, y, z) == (w1, x1, y1, z1):
                        continue
                    if (w1, x1, y1, z1) in active:
                        count += 1
    return count


def cycle(active):
    new_active = active.copy()
    min_w = min([coord[0] for coord in new_active])
    max_w = max([coord[0] for coord in new_active])
    min_x = min([coord[1] for coord in new_active])
    max_x = max([coord[1] for coord in new_active])
    min_y = min([coord[2] for coord in new_active])
    max_y = max([coord[2] for coord in new_active])    
    min_z = min([coord[3] for coord in new_active])
    max_z = max([coord[3] for coord in new_active])
    for w in range(min_w - 1, max_w + 2):
        for x in range(min_x - 1, max_x + 2):
            for y in range(min_y - 1, max_y + 2):
                for z in range(min_z - 1, max_z + 2):
                    num_around = active_surrounding(active, w, x, y, z)
                    if (w, x, y, z) in active and num_around not in (2, 3):
                        new_active.remove((w, x, y, z))
                    if (w, x, y, z) not in active and num_around == 3:
                        new_active.add((w, x, y, z))
    return new_active

def cycle_count(active, count):
    new_active = active.copy()
    for _ in range(count):
        new_active = cycle(new_active)
    return new_active

print('6 cycles', len(cycle_count(active_cubes, 6)))