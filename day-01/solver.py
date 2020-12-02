data = [int(x) for x in open('input').read().split()]

datasize = len(data)
target = 2020

# Part 1
found = False
for x in range(datasize - 1):
    for y in range(x + 1, datasize):
        if data[x] + data[y] == target:
            found = True
            break
    if found:
        break

print('X', x, 'Y', y)
print(data[x] * data[y])


# Part 2
found = False
for x in range(datasize - 2):
    for y in range(x + 1, datasize - 1):
        for z in range(y + 1, datasize):
            if data[x] + data[y] + data[z] == target:
                found = True
                break
        if found:
            break
    if found:
        break

print('X', x, 'Y', y, 'Z', z)
print(data[x] * data[y] * data[z])