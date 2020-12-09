import copy
f = open('day08.txt', 'r')
data = f.read()
data = data.split('\n')

commandList = [d.split() for d in data]
for c in commandList:
        c.append(False)

def run_prog(commands):
    infinite = False
    increment = 1
    pos = 0
    acc_count = 0
    
    while not infinite:
        if commands[pos][2]:
            infinite = True
        else:
            commands[pos][2] = True
            step = commands[pos]
            acc_count += int(step[1]) if step[0] == 'acc' else 0
            pos += int(step[1]) if step[0] == 'jmp' else increment
            if (pos >= len(commands)):
                infinite = True
            
            
    return [acc_count, pos]

part1 = run_prog(commandList)

print(part1)

length = len(commandList) - 1
for index in range(length):
    for c in commandList:
        c[2] = False
    cmd = copy.deepcopy(commandList)

    if cmd[index][0] == 'acc':
        continue
    elif cmd[index][0] == 'jmp':
        cmd[index][0] = 'nop'
    else:
        cmd[index][0] = 'jmp'
    part2 = run_prog(cmd)
    if part2[1] >= len(cmd) :
        print(part2)
        break