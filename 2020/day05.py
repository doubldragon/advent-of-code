f = open('day05.txt', 'r')

data = f.read()
data = data.split('\n')
numRows = 128
maxId = 0
maxRow = 0
maxSeat = 0
idList = []

def findRow(rowCode):
    max = numRows
    min = 0
    
    for r in rowCode:
        step = (max-min)/2
        if r == 'B':
            min += step
        else:
            max -= step
    return min if rowCode[6] == 'F' else max - 1

def findSeat(seatCode):
    min = 0
    max = 8
    for s in seatCode:
        step = (max-min)/2
        if s == 'R':
            min += step
        else:
            max -= step
    return min if seatCode[2] == 'L' else max - 1

for d in data:
    rowCode, seatCode = d[:-3], d[-3:]
    row = round(findRow(rowCode))
    seat = round(findSeat(seatCode))
    id = row * 8 + seat
    idList.append(id)

    if id > maxId:
        maxId = id
        maxRow = row
        maxSeat = seat
print('MAX ID = ' + str(maxId))
print('MAX Row = ' + str(maxRow) + ' ' + str(maxSeat))
idList.sort()
for id in idList:
    if id + 1 not in idList:
        print(id +1)
        break