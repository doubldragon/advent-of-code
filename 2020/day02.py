import re

f = open('day02.txt', 'r')

data = f.read()
x = range(4)
rough_list = re.split(': |-|\n| ', data)
chunks = [rough_list[x:x+4] for x in range(0, len(rough_list), 4)]
valid = 0

def split(word):
    return [char for char in word]

for p in chunks:
    list = split(p[3])
    check = [list[int(p[0])-1],list[int(p[1])-1]]
    if ((check[0] == p[2] and check[1] != p[2]) or (check[0] != p[2] and check[1] == p[2])):
        valid += 1

print(valid)
