import sys
from itertools import combinations

F = []
Counts = []
data = sys.stdin.readlines()
minsup = int(data[0])
sets = data[1:]
all = ''
for i in range(len(sets)):
    all += sets[i]

sorted_all = sorted(all.split())
collect = {}

for i in sorted_all:
    if i not in collect:
        if sorted_all.count(i) >= minsup:
            collect[i] = sorted_all.count(i)

F.append(list(collect.keys()))
Counts.append(list(collect.values()))
all = all.split('\n')

for num in range(2, max([len(i.split()) for i in all])):
    FNext = []
    count = []
    comb = combinations(F[num - 2], 2)
    for i in list(comb):
        sum = 0

        for j in range(len(i[0].split())):
            sum += int(i[0].split()[j] != i[1].split()[j])

        if sum == 1:
            '''generate candidats'''
            tempc = list(set(i[0].split() + i[1].split()))

            '''print(tempc)'''
            '''test and prune candidates'''
            tempcomb = combinations(tempc, num - 1)
            flag = False

            for k in list(tempcomb):

                if flag == True:
                    break
                fcomb = combinations(F[num - 2], 1)
                '''print(F[num - 2])'''
                for p in list(fcomb):
                    '''print('asdfa',k,set(p[0].split()))'''
                    if set(k) == set(p[0].split()):
                        flag = True
                        break
            '''test frequency'''

            if flag:
                sup = 0

                for p in all:

                    if set(tempc) <= set(p.split()):
                        sup += 1
                if sup >= minsup:
                    text = ''
                    count.append(sup)
                    '''for i in sorted(tempc):'''
                    text = ' '.join(sorted(tempc))
                    FNext.append(text)
    F.append(FNext)
    Counts.append(count)
    pattern = {}

    for i in range(len(F)):
        for j in range(len(F[i])):
            pattern[F[i][j]] = Counts[i][j]

keylist = sorted(list(pattern.keys()))

value = [pattern[i] for i in keylist]
fp = []
support = []


def unique(x):
    buffer = []
    for i in range(len(x)):
        if x[i] not in buffer:
            buffer.append(x[i])
    return (buffer)


def where(x, value):
    index = []
    for i in range(len(x)):
        if x[i] == value:
            index.append(i)
    return (index)


for i in sorted(unique(value), reverse=True):
    buffer = [keylist[i] for i in where(value, i)]
    for ttt in buffer:
        fp.append(ttt)
    for m in buffer:
        sys.stdout.write(str(pattern[m]) + ' ' + '[' +
                         m + ']' + '\n')
        support.append(pattern[m])
sys.stdout.write('\n')

'''part2'''
test = []
for i in range(len(fp)):
    flag = True
    for j in range(len(fp)):
        if i != j:
            if set(fp[i].split()) < set(fp[j].split()):
                if support[i] == support[j]:
                    flag = False
                    break
    if flag:
        test.append(i)
for m in test:
    sys.stdout.write(str(support[m]) + ' ' + '[' + fp[m] + ']')
    sys.stdout.write('\n')
sys.stdout.write('\n')

'''part3'''
test = []
for i in range(len(fp)):
    flag = True
    for j in range(len(fp)):
        if i != j:
            if set(fp[i].split()) < set(fp[j].split()):
                flag = False
                break
    if flag:
        test.append(i)
for m in test:
    sys.stdout.write(str(support[m]) + ' ' + '[' + fp[m] + ']')
    sys.stdout.write('\n')
