user_number = int(input('Введите целое положительное число: '))

r = -1
while user_number > 10:
    big_number = user_number % 10
    user_number //= 10
    if big_number > r:
        r = big_number
print(r)


