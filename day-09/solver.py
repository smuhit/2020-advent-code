data = [int(x) for x in open('input.txt').read().split()]

# Part 1

preamble_length = 25

def test_in_preamble(idx):
    test = data[idx]
    valid = False
    for x in data[idx - preamble_length:idx]:
        if x != test - x and (test - x) in data[idx - preamble_length:idx]:
            valid = True
            break
    return valid

for idx, _ in enumerate(data[preamble_length:len(data)]):
    shifted_index = idx + preamble_length
    if not(test_in_preamble(shifted_index)):
        break

print('Does not have 25 length preamble', data[shifted_index])

# Part 2

goal = data[shifted_index]
contiguous = []

for test in data:
    contiguous.append(test)
    while sum(contiguous) > goal:
        contiguous.pop(0)
    if sum(contiguous) == goal:
        break

print('Sum of smallest and largest in contiguous set', min(contiguous) + max(contiguous))