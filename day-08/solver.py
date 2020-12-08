from copy import copy

data = open('input.txt').read().split('\n')


position = 0
accumulator = 0

def jump(x):
    global position
    position += x

def no_op(_):
    jump(1)

def accumulate(x):
    global accumulator
    accumulator += x
    jump(1)

operations = {
    'acc': accumulate,
    'nop': no_op,
    'jmp': jump
}

def run(dataset):
    visited = set()
    while position not in visited and position < len(data):
        visited.add(position)
        operator, value = dataset[position].split()
        operations[operator](int(value))

# Part 1
run(data)
print('Accumulated', accumulator)


# Part 2
positions_to_change = [pos for pos, val in enumerate(data) if val.startswith('nop') or val.startswith('jmp')]

for position_to_change in positions_to_change:
    position = 0
    accumulator = 0
    data_copy = copy(data)
    operator, value = data_copy[position_to_change].split()
    if operator == 'jmp':
        operator = 'nop'
    else:
        operator = 'jmp'
    data_copy[position_to_change] = f'{operator} {value}'
    run(data_copy)
    if position >= len(data_copy):
        break

print('Accumulated', accumulator)