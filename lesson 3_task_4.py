''' 1 способ с помощью оператора **'''
def my_func(x, y):
    num = x**y
    return num
print(my_func(int(input('положительное число: ')), int(input('отрицательное число: '))))

''' 2 способ с помощью цикла'''
# def my_func(x, y):
#     while y <= 0:
#         a = x * x
#         y = y + 1
#     num = 1 / a
#     return num
#
# print(my_func(int(input('положительное число: ')), int(input('отрицательное число: '))))

''' 3 способ - с помощью функции pow'''
# def my_func(x, y):
#     num = pow(x, y)
#     return num
# print(my_func(int(input('положительное число: ')), int(input('отрицательное число: '))))

