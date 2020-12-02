data = open('input').read().split('\n')

data_split = []
for datum in data:
    parts = datum.split(' ')
    low, high = [int(x) for x in parts[0].split('-')]
    letter = parts[1][0]
    password = parts[2]
    data_split.append((low, high, letter, password))

# Part 1
count_valid = 0
for datum in data_split:
    low, high, letter, password = datum
    letter_count = password.count(letter)
    if low <= letter_count and letter_count <= high:
        count_valid += 1

print('Valid passwords:', count_valid)

# Part 2
count_valid = 0
for datum in data_split:
    low, high, letter, password = datum
    if (password[low-1] == letter) != (password[high-1] == letter):
        count_valid += 1

print('Valid passwords:', count_valid)
