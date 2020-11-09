from itertools import count
f_obj = open(r'05112020.txt', 'r')
f_obj.seek(0)
l = f_obj.readlines()
print('колличество строк: ', (len(l)))
f_obj.seek(0)
lines = f_obj.readlines()

for line in lines:
    y = line.strip()
    print(y)
    a = line.split()
    print(len(a))
f_obj.close()