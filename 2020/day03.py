f = open('day03.txt', 'r')

data = f.read()
data = data.split('\n')


x=3
y=0
x_steps= [1,3,5,7]
treeArray = []
count = 0
not_trees=0

def splitRow(row):
    return [r for r in row]

def checkForTrees(row, index):
    currentRow = splitRow(row)
    return currentRow[index] == '#'

for x_step in x_steps:
    x=x_step
    trees= 0
    iterData = iter(data)
    next(iterData)
    for d in iterData:
        count += 1
        currentRow = splitRow(d)
        if checkForTrees(d,x):
            trees += 1
            
        x += x_step
        if (x >= len(currentRow)):
            x -= len(currentRow)
    treeArray.append(trees)

iterData = iter(data)
print(next(iterData))
x_step = 1
trees=0
x=1
s = ""
for index, d in enumerate(iterData):
    if index % 2 == 0:
        print(d)
        continue
    currentRow = splitRow(d)
    if checkForTrees(d,x):
        
        currentRow[x] = 'X'
        trees +=1
    else:
        currentRow[x] = 'O'
    print (s.join(currentRow))
    x += x_step
    if (x >= len(currentRow)):
        x -= len(currentRow)
treeArray.append(trees)
totalTrees = 1
for tree in treeArray:
    totalTrees *= tree

print(treeArray)
print(totalTrees)