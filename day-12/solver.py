data = open('input.txt').read().split()

# Part 1
starting_location = [0, 0]
heading = 0

def move_absolute(val, direction):
    direction_map = {
        'N': (0, val),
        'S': (0, -val),
        'E': (1, val),
        'W': (1, -val)
    }

    idx, abs_val = direction_map[direction]

    starting_location[idx] += abs_val

def move_relative(val):
    direction_map = {
        0: (1, val),
        1: (0, val),
        2: (1, -val),
        3: (0, -val)
    }

    idx, abs_val = direction_map[heading]

    starting_location[idx] += abs_val


def turn(val, direction):
    global heading
    turn_map = {
        'L': val,
        'R': -val
    }

    incrementor = turn_map[direction]
    amount = incrementor // 90

    heading = (heading + amount) % 4


operations = {
    'N': lambda x: move_absolute(x, 'N'),
    'S': lambda x: move_absolute(x, 'S'),
    'E': lambda x: move_absolute(x, 'E'),
    'W': lambda x: move_absolute(x, 'W'),
    'L': lambda x: turn(x, 'L'),
    'R': lambda x: turn(x, 'R'),
    'F': lambda x: move_relative(x),
}

for datum in data:
    operator = datum[0]
    val = int(datum[1:])
    operations[operator](val)

print('Manhattan distance', abs(starting_location[0]) + abs(starting_location[1]))

# Part 2
starting_location = [1, 10]  # Waypoint
ship_location = [0, 0]

def waypoint_turn(val, direction):
    turn_map = {
        'L': val,
        'R': -val
    }

    rotation_map = {
        0: (starting_location[0], starting_location[1]),
        1: (starting_location[1], -starting_location[0]),
        2: (-starting_location[0], -starting_location[1]),
        3: (-starting_location[1], starting_location[0]),
    }

    incrementor = turn_map[direction]
    amount = (incrementor // 90) % 4
    starting_location[0], starting_location[1] = rotation_map[amount]

def ship_move(val):
    ship_location[0] += starting_location[0] * val
    ship_location[1] += starting_location[1] * val

operations = {
    'N': lambda x: move_absolute(x, 'N'),
    'S': lambda x: move_absolute(x, 'S'),
    'E': lambda x: move_absolute(x, 'E'),
    'W': lambda x: move_absolute(x, 'W'),
    'L': lambda x: waypoint_turn(x, 'L'),
    'R': lambda x: waypoint_turn(x, 'R'),
    'F': lambda x: ship_move(x),
}

for datum in data:
    operator = datum[0]
    val = int(datum[1:])
    operations[operator](val)

print('Manhattan distance', abs(ship_location[0]) + abs(ship_location[1]))
