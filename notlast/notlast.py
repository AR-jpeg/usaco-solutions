"""
ID: araoudu1
LANG: PYTHON3
PROG: notlast
"""

fin = open('notlast.in')
fout = open('notlast.out', 'w')

cows = [cow.split() for cow in fin.readlines()[1::]]

total_milk = {}

for cow in cows:
    name = cow[0]
    amount = int(cow[1])
    if name not in total_milk:
        total_milk[name] = 0

    total_milk[name] += amount

allamounts = list(total_milk.values())
sorted_amounts = sorted(allamounts)

second = 0
secondname = ''
minimum = sorted_amounts[0]
for n in sorted_amounts[1::]:
    if n > minimum:
        second = n
        break

count = 0
for n in sorted_amounts[1::]:
    if n == second:
        count += 1

for cow in total_milk:
    if total_milk[cow] == second:
        secondname = cow

if len(cows) == 1:
    fout.write(cows[0][0])
else:
    if count == 1:
        fout.write(secondname)
    else:
        fout.write('Tie')

fout.write('\n')
fout.close()
