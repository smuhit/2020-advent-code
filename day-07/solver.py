data = open('input.txt').read().split('\n')

bag_dict = {}

for datum in data:
    bag, values = datum.split(' bags contain ')
    bag_dict[bag] = {}
    if not values.startswith('no other'):
        value_list = values.split(', ')
        for value in value_list:
            value = value.rsplit(' ', 1)[0]
            num, subbag = value.split(' ', 1)
            bag_dict[bag][subbag] = int(num)

# Part 1

def find_outer_bags(goal):
    found_bags = set()
    for bag in bag_dict:
        if goal in bag_dict[bag]:
            found_bags.add(bag)
            found_bags |= find_outer_bags(bag)
    return found_bags

print('Count', len(find_outer_bags('shiny gold')))


# Part 2

def count_bags(goal, num):
    count = num
    for bag in bag_dict[goal]:
        count += count_bags(bag, bag_dict[goal][bag]) * num
    return count

print('Count', count_bags('shiny gold', 1) - 1)