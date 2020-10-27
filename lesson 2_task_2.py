my_dict = []
q = input('Хотите ввести значение? Y / N: ')
m = q.lower()

while m == 'y':
    q = input('Хотите ввести значение? Y / N: ').lower()
    while m == 'y':
        user_list = input('Внесите данные: ')
        my_dict.append(user_list)
        print(my_dict)
        break
print(q)
