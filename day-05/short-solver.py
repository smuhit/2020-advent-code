# After solving, realized that I could get the code much shorter

data = set([int(x.translate(str.maketrans('FBLR', '0101')), base=2)
            for x in open('input.txt').read().split()])

print('Part 1', max(data))

print('Part 2', (set(list(range(min(data), max(data) + 1))) - data).pop())
