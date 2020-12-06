data = open('input.txt').read().split('\n')


# Part 1
count = 0
answered = set()
for datum in data:
    if datum == '':
        count += len(answered)
        answered = set()
    for letter in datum:
        answered.add(letter)

print('Count', count)

# Part 1
count = 0
num_in_group = 0
answered = set()
for datum in data:
    persons_answer = set()
    num_in_group += 1
    if datum == '':
        count += len(answered)
        answered = set()
        num_in_group = 0
    for letter in datum:
        persons_answer.add(letter)
    if num_in_group == 1:
        answered = persons_answer
    else:
        answered = answered.intersection(persons_answer)

print('Count', count)
