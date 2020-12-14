raw_data = open('input.txt').read().split('\n')

data = {}
current_mask = None
current_mems = []
for datum in raw_data:
    if datum.startswith('mask'):
        if current_mask:
            data[current_mask] = current_mems
        current_mask = datum.split(' = ')[-1]
        current_mems = []
    elif datum.startswith('mem'):
        mem, val = datum.split(' = ')
        mem = mem.split('[')[-1].split(']')[0]
        current_mems.append((int(mem), int(val)))
data[current_mask] = current_mems

# Part 1

def mask_bits(val, mask):
    val = list(format(val, 'b'))
    val = ['0'] * (len(mask) - len(val)) + val

    construct = []
    for v_bit, m_bit in zip(val, mask):
        if m_bit in ('0', '1'):
            construct.append(m_bit)
        else:
            construct.append(v_bit)

    return int(''.join(construct), base=2)


mask_mem = {}
for mask in data:
    for mem, value in data[mask]:
        mask_mem[mem] = mask_bits(value, mask)
summation = 0
for mem in mask_mem:
    summation += mask_mem[mem]

print(summation)

# Part 2


def recurse_counter(val, mask, idx):
    construct = val.copy()
    if idx >= len(mask):
        return [construct]

    construct_container = []
    if mask[idx] == '0':
        construct_container +=  recurse_counter(construct, mask, idx + 1)
    elif mask[idx] == '1':
        construct[idx] = '1'
        construct_container +=  recurse_counter(construct, mask, idx + 1)
    elif mask[idx] == 'X':
        construct[idx] = '0'
        construct_container +=  recurse_counter(construct, mask, idx + 1)
        construct[idx] = '1'
        construct_container +=  recurse_counter(construct, mask, idx + 1)

    return construct_container


def mask_bits_address(address, mask):
    val = list(format(address, 'b'))
    val = ['0'] * (len(mask) - len(val)) + val

    construct_container = recurse_counter(val, mask, 0)
    
    return [int(''.join(construct), base=2) for construct in construct_container]

mask_mem = {}
for mask in data:
    for mem, value in data[mask]:
        all_addresses = mask_bits_address(mem, mask)
        for address in all_addresses:
            mask_mem[address] = value

summation = 0
for mem in mask_mem:
    summation += mask_mem[mem]

print(summation)
