f = open('day09.txt', 'r')
data = f.read()
data = data.split('\n')
data.pop()
data = [int(x) for x in data]
preamble = 25
vuln = 0

def findBase(number, searchRange):
    inRange = False
    for iter in searchRange:
        if int(number) - int(iter) in searchRange:
            inRange = True
            break;
    return inRange
    
for index, num in enumerate(data[preamble:]):
    endRange = int(index) + preamble
    inRange = findBase(num, data[index:endRange])
    if not inRange:
        print(num)
        vuln = num
        break;

def findContiguous(vuln):
    for i in range(len(data)):
        sum = 0
        count = 0
        while sum <= vuln:
            sum += data[i+count]
            count +=1
            if  sum == vuln:
                return [i,(i + count)]
sumRange = findContiguous(vuln)
print(sumRange)
snip = data[sumRange[0]:sumRange[1]]
print(max(snip) + min(snip))