name = 'Ольга'
surname = 'Паршина'
age = 34
print('Привет!')
print('Давай познакомимся )')
print(f'Меня зовут {name} {surname}. Мне {age} года.')
user_name = str(input('Введи свое имя:'))
user_age = int(input('Введи свой возраст:'))
print(f'Привет {user_name}. Рада познакомиться)')
if user_age < age:
    print('Мне чуть больше )')
elif user_age == age:
    print('мне тоже столько')
else:
    print('ты мудрее меня')

numb_1 = int(input('Введи 1 число: '))
numb_2 = int(input('Введи 2 число: '))

if numb_1 < numb_2:
    print('Первое число меньше второго')
elif numb_1 == numb_2:
    print('Числа равны')
else:
    print('Первое число больше второго')