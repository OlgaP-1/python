from math import ceil
class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)
    def __add__(self, other):
        return f'объединение двух клеток: {self.quantity + other.quantity} ячеек'
    def __sub__(self, other):
        return f'{self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print("разность количества ячеек 2-х клеток меньше 0")}'
    def __mul__(self, other):
        return f'произведение клеток: {self.quantity * other.quantity} ячеек'
    def __truediv__(self, other):
        return f'целочисленное деление клеток: {ceil(self.quantity / int(other.quantity))} ячеек'
    def make_order(self, num):
        l = []
        l.append(self.quantity * '*')
        for i in l:
            while len(l) == num:
                i = i[0].split(' ')
            for el in i:
                el = el
        s = 0
        (((el * num) + '\n') * int(len(i) / num) + (el * s))
        if int(len(i) % num) != 0:
            s = (len(i) % num)
            (((el * num) + '\n') * int(len(i) / num) + (el * s))
        return f'{(((el * num) + "/n") * int(len(i) / num) + (el * s))}'

cells1 = Cell(27)
cells2 = Cell(9)
cells3 = 5
print(cells1.quantity.__add__(4))
print(cells1.quantity.__sub__(7))
print(cells1.quantity.__mul__(4))
print(cells1.quantity.__truediv__(4))
print(cells1.make_order(4))