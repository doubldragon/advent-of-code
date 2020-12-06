
f = open('day01a.txt', 'r')

data = f.read()

data_int = []

for each in data.split():
    data_int.append(int(each))

result2 = 0
result3 = 0

for a in data_int:
    for b in data_int:
        if a + b == 2020:
            result2 = a * b
        for c in data_int:
            if a + b + c == 2020:
                result3 = a * b * c
                

print(result2)
print(result3)
