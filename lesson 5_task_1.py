f = open(r'04112020.txt', 'w')

while True:
    f = open(r'04112020.txt', 'a')
    a = f.write(input('ввод: ') + '\n')
    if a == 1:
        break
f.close()
