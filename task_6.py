day_a = int(input('Введите колличество пройденных километров за один день: '))
day_b = int(input('Введите желаемое расстояние в километрах: '))
km_day = int(day_a * 0.1 + day_a)
day_x = 1
while km_day < day_b:
    if km_day < day_b:
        km_day = km_day * 0.1 + km_day
        day_x += 1
    else:
        continue

print(f'На {day_x} день спортсмен достигнет результата — не менее {day_b} км.')
