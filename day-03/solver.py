data = open('input').read().split()


# Part 1
trees = 0
x = 0
for datum in data:
    if x >= len(datum):
        x -= len(datum)
    if datum[x] == '#':
        trees += 1
    x += 3

print('Trees:', trees)

# Part 2 (Brute force -- because tired)
solution = trees

trees = 0
x = 0
for datum in data:
    if x >= len(datum):
        x -= len(datum)
    if datum[x] == '#':
        trees += 1
    x += 1

solution *= trees

trees = 0
x = 0
for datum in data:
    if x >= len(datum):
        x -= len(datum)
    if datum[x] == '#':
        trees += 1
    x += 5

solution *= trees

trees = 0
x = 0
for datum in data:
    if x >= len(datum):
        x -= len(datum)
    if datum[x] == '#':
        trees += 1
    x += 7

solution *= trees

trees = 0
x = 0
for y, datum in enumerate(data):
    if y % 2 != 0:
        continue
    if x >= len(datum):
        x -= len(datum)
    if datum[x] == '#':
        trees += 1
    x += 1

solution *= trees


print('Solution:', solution)