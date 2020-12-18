import math

data = open('input.txt').read().split('\n')

# Part 1

def evaluate(line):
    operator_map = {
        '+': sum,
        '*': math.prod
    }
    stack = []
    working_val = 0
    current_operator = sum

    for val in line:
        if val not in ('+', '*', '(', ')'):
            working_val = current_operator([working_val, int(val)])
        elif val in ('+', '*'):
            current_operator = operator_map[val]
        elif val == '(':
            stack.append((working_val, current_operator))
            working_val = 0
            current_operator = sum
        elif val == ')':
            old_val, current_operator = stack.pop()
            working_val = current_operator([working_val, old_val])
    return working_val


summation = 0

for line in data:
    line = ''.join(line.split(' '))
    summation += evaluate(line)

print('Evaluate', summation)

# Part 2

def evaluate(line):
    operator_map = {
        '+': sum,
        '*': math.prod
    }
    stack = []
    working_val = 0
    current_operator = sum
    idx = 0

    while idx < len(line):
        val = line[idx]
        if val not in ('+', '*', '(', ')'):
            if current_operator == sum:
                working_val = current_operator([working_val, int(val)])
            else:
                stack.append((working_val, current_operator))
                working_val = int(val)
                current_operator = sum
        elif val in ('+', '*'):
            current_operator = operator_map[val]
        elif val == '(':
            paren_stack = []
            balance = 1
            while True:
                idx += 1
                if line[idx] == '(':
                    balance += 1
                if line[idx] == ')':
                    balance -= 1
                if not balance:
                    break
                paren_stack.append(line[idx])

            if current_operator == sum:
                working_val = current_operator([working_val, evaluate(paren_stack)])
            else:
                stack.append((working_val, current_operator))
                working_val = evaluate(paren_stack)
                current_operator = sum
        idx += 1
    for old_val, current_operator in stack:
        working_val = current_operator([working_val, old_val])
    return working_val

summation = 0

for line in data:
    line = ''.join(line.split(' '))
    summation += evaluate(line)

print('Evaluate', summation)
