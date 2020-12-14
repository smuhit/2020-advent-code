timestamp, bus_ids = open('input.txt').read().split()


# Part 1

timestamp = int(timestamp)

buses_in_service = [int(x) for x in bus_ids.split(',') if x != 'x']

bus_timetable_map = {}

for bus in buses_in_service:
    bus_timetable_map[bus] = bus - (timestamp % bus or bus)

bus_to_take = min(bus_timetable_map.keys(), key=(lambda k: bus_timetable_map[k]))

print('ID * wait', bus_to_take * bus_timetable_map[bus_to_take])


# Part 2 -- 
# Chinese Remainder Theorem borrowed heavily from 
# https://medium.com/@astartekraus/the-chinese-remainder-theorem-ea110f48248c
import math

bus_offset = [(int(x), idx) for idx, x in enumerate(bus_ids.split(',')) if x != 'x']
vals = [x for x, _ in bus_offset]
remainders = [x - (idx % x or x) for x, idx in bus_offset]

def extended_euclid(x, y):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while y > 0:
        q, x, y = x // y, y, x % y
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return x0, y0

def invmod(a, m):
    x, y = extended_euclid(a, m)
    return x % m

def chinese_remainder_gauss(n, a):
    result = 0
    product = math.prod(n)
    for i in range(len(n)):
        ai = a[i]
        ni = n[i]
        bi = product // ni
        result += ai * bi * invmod(bi, ni)
    return result % product

print(chinese_remainder_gauss(vals, remainders))