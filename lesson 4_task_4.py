my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
n = []
# n = [my_list[i] for i in list(range(0, len(my_list), 1)) if my_list[i] not in n]

for i in list(range(1, len(my_list), 1)):
    if my_list[i] not in n:
        n.append(my_list[i])

print(n)
