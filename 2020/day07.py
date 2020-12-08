f = open('day07.txt', 'r')
data = f.read()
data = data.split('\n')
rules = [d.split(' bags contain ') for d in data]
final_bags = []
initial_bag = 'shiny gold'

def bag_search(term):
    return [r[0] for r in rules if r[1].find(term) != -1]

bags_to_check = bag_search(initial_bag)

while len(bags_to_check) > 0:
    bag = bags_to_check.pop()
    if bag not in final_bags:
        final_bags.append(bag)
        bags_to_check += bag_search(bag)

print(len(final_bags))

shiny_bag = [r[1] for r in rules if r[0] == initial_bag]
total_bags = 0
def parse_bag_list(list):
    return list.split(', ') if len(list) > 1 else list

bags_to_check = parse_bag_list(shiny_bag[0])

def get_next_bags(query):
    next_bags = [r[1] for r in rules if r[0] == query]
    return parse_bag_list(next_bags[0])
    
def is_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

while len(bags_to_check) > 0:
    bag_info = bags_to_check.pop().replace(' bags', '').replace(' bag', '').replace('.', '').split(' ', 1)
    
    if is_int(bag_info[0]):
        total_bags += int(bag_info[0])
    else:
        continue
    for x in range(int(bag_info[0])):
        bags_to_check += get_next_bags(bag_info[1])

print(total_bags)
    
