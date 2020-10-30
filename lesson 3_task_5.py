while True:
    if input('Выход - Q \n Любая клавиша - продолжить').upper() == 'Q':
        break
    user_num = (input('числа: ')).split()
    summa = 0
    a = 1

    for i in user_num:
        summa += int(i)
    print(summa)