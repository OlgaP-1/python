f = open('05112020.txt', encoding='utf-8')
f.seek(0)
lines = f.readlines()
y = []
for el in lines:
    a = el.split()
    b = a[3: 5]
    for x in b:
        x = int(x)
        y.append(x)
        if x < 20000:
            print(a[0:3])
print('средняя заработная плата составляет: ', sum(y) / len(lines))
f.close()