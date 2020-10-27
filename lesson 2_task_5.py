my_dict = []
q = input('Хотите ввести значение? Y / N: ')
m = q.lower()

if q == 'y':
    while True:
        user_list = input('Внесите данные: ')
        my_dict.append(user_list)
        print(my_dict)
        m = input('хотите добавить? ')
        if m == 'n':
            break
    else:
        print(list(my_dict))
        m = input('хотите продолжить? ')
        if m == 'y':
            True
else:
    print("ОТКАЗ ОТ ВВОДА")
print('отказ от ввода \n' + 'Список: ')
new_list = sorted(my_dict)
# print(new_list)
new_list.reverse()
print(', '.join(new_list))


