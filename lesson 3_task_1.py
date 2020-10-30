try:
    def user_num(var_1, var_2):
        a = var_1 / var_2
        return a
    print(user_num(int(input('первое число: ')), int(input('второе число: '))))
except ZeroDivisionError:
    print('деление на ноль')
except ValueError:
    print('введено не число')
except TypeError:
    print('введено не число')
except UnboundLocalError:
    print('что-то пошло не так')
except Traceback:
    print('введено не число')

print(user_num)