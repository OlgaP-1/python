f = open('text3.txt', encoding='utf-8')
f.seek(0)
lines = f.readlines()
print(lines)

with open('text4.txt', 'w', encoding='utf-8') as f_obj:
    for line in lines:
        y = line.strip()
        y = y.replace('One', 'Один')
        y = y.replace('Two', 'Два')
        y = y.replace('Three', 'Три')
        y = y.replace('Four', 'Четыре')
        file = f_obj
        print(y, file=f_obj)
