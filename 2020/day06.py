from collections import OrderedDict
f = open('day06.txt', 'r')

data = f.read()
data = data.split('\n\n')
sum=0
all_sum = 0
groups = [d.split('\n') for d in data]
def common_answers(string, l):
    lst = sorted(string)
    res = [(el, lst.count(el)) for el in lst]
    ordered = list(OrderedDict(res).items())
    errbody = 0
    for o in ordered:
        if(o[1] == l):
            errbody += 1
    return errbody


for g in groups:
    raw = ''.join(g)
    str = ''.join(set(raw))
    sum += len(str)
    all_sum += common_answers(raw, len(g))
    
print(sum)
print(all_sum)