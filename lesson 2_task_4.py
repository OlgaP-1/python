data = input('Ввод: ')
step = data[::1]

n = step.split()
# print(n[::1])
# print(len(n))
len_data = len(n)
i = -1

for ind, len_data in enumerate(n, 1):
    b = int(len(n))
    i = -1
    while i < b:
        i = i + 1
        c = n[i]

        if len(c) > 9:
           len_data = len_data[0:10:1]
           break
        else:
            continue

    else:
        print(i)
    print(ind, len_data)







