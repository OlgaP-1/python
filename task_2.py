times = int(input('Введите число для преобразования: '))
day = times // 86400
hour = times // 3600
minuts = times // 60
second = times * 60

print(f'число преобразовано в вид дни:чч:мм:сс: {day}:{hour}:{minuts}:{second}')
