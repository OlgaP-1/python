f = open('text5.txt', 'w+', encoding='utf-8')
f.write('1 2 3 5 6')
f.seek(0)
lines = f.readlines()
for el in lines:
    el = el.split()
    s = []
    for x in el:
        x = int(x)
        s.append(x)
print('сумма чисел равна: ', sum(s))
f.close()


