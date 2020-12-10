data = [int(x) for x in open('input.txt').read().split()]


# Part 1

sorted_data = sorted(data)

jolt_differences = {
    1: 1,
    2: 0,
    3: 1
}


for x in range(len(sorted_data) - 1):
    jolt_differences[sorted_data[x + 1] - sorted_data[x]] += 1

print('Jolt calculation', jolt_differences[1] * jolt_differences[3])


# Part 2

set_data = set(data)

cache_value = {}

def find_arrangments(val):
    if val in cache_value:
        return cache_value[val]
    downstream = 0
    for possibility in (val + 1, val + 2, val + 3):
        if possibility in set_data:
            downstream += find_arrangments(possibility)
    if downstream == 0:
        downstream = 1
    cache_value[val] = downstream
    return downstream

print('Variations', find_arrangments(0))
