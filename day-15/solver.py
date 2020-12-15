data = '5,1,9,18,13,8,0'

data_list = [int(x) for x in data.split(',')]

def game(turns):
    seen = {}
    for idx, datum in enumerate(data_list):
        seen[datum] = idx + 1
    last = 0
    pre_last = data_list[-1]
    for idx in range(len(data_list) + 2, turns + 1):
        print(idx, end='\r')
        pre_last = last
        last = (idx - 1 - seen[last]) if last in seen else 0
        seen[pre_last] = idx - 1
    return last


# Part 1
print('2020: ', game(2020))

# Part 2
print('30000000th: ', game(30000000))