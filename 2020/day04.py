import re
f = open('day04.txt', 'r')

data = f.read()
data = data.split('\n\n')
id_list = []
for d in data:
    subUnit = {}
    d = d.replace('\n', ' ')
    d = d.split()
    for pair in d:
        tuple = pair.split(':')
        subUnit[tuple[0]] = tuple[1]
    id_list.append(subUnit)

def byr_check(byr):
    if not byr:
         return False
    else:
        return True if 1920 <= int(byr) <= 2002 else False

def iyr_check(iyr):
    if not iyr:
        return False
    else:
        return True if 2010 <= int(iyr) <= 2020 else False

def eyr_check(eyr):
    if not eyr:
        return False
    else:
        return True if 2020 <= int(eyr) <= 2030 else False

def cid_check(id):
    target = id.get('cid', None)
    return False if target else True

def hgt_check(height):
    if not height:
        return False
    height, unit = height[:-2], height[-2:]
    
    if unit not in ['cm', 'in']:
        return False
    height = int(height)
    if unit == 'cm':
        return True if 150 <= height <= 193 else False
    else:
        return True if 59 <= height <= 76 else False

def hcl_check(hcl):
    if not hcl:
        return False
    if hcl[0] == '#' and len(hcl) == 7:
        match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hcl)
        return True if  match else False
    else:
        return False

def ecl_check(ecl):
    if not ecl:
        return False
    valid_ecl = ['amb', 'blu','brn','gry', 'grn', 'hzl', 'oth']
    return True if ecl in valid_ecl else False

def pid_check(pid):
    if not pid:
        return False
    return True if len(pid) == 9 else False

def id_check(id):
    if len(id) < 7:
        return False
    if len(id) == 7 and not cid_check(id):
        return False
    if not byr_check(id.get('byr', None)):
        return False
    if not iyr_check(id.get('iyr', None)):
        return False
    if not eyr_check(id.get('eyr', None)):
        return False
    if not hgt_check(id.get('hgt', None)):
        return False
    if not hcl_check(id.get('hcl', None)):
        return False
    if not ecl_check(id.get('ecl', None)):
        return False
    if not pid_check(id.get('pid', None)):
        return False
    return True
    


validCount = 0

for id in id_list:
    if id_check(id):
        validCount += 1

print(validCount)