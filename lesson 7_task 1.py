class Matrix:
    def __init__(self):
        self.data = []
    def __add__(self, other):
        self.data.append(other)
        return self
    def __str__(self):
        return f'{self.data}'
list_1 = Matrix()
data_list1 = 31
data_list2 = 22
data_list3 = 51
list_2 = Matrix()
data_list4 = 86
data_list5 = 37
data_list6 = 43
list_3 = Matrix()
data_list7 = -50
data_list8 = 0
data_list9 = 25
print('матрица 1')
list_1 + data_list1 + data_list2 + data_list3
list_2 + data_list4 + data_list5 + data_list6
list_3 + data_list7 + data_list8 + data_list9
print('\n', list_1, '\n', list_2, '\n', list_3)

print('\n', 'матрица 2')

list_4 = Matrix()
data_list17 = 31
data_list18 = 22
data_list19 = 51
data_list20 = 200
list_5 = Matrix()
data_list21 = 86
data_list22 = 37
data_list23 = 43
data_list24 = -42
list_6 = Matrix()
data_list25 = -50
data_list26 = 0
data_list27 = 25
data_list28 = -87
list_7 = Matrix()
data_list13 = 18
data_list14 = 32
data_list15 = 79
data_list16 = 145
list_4 + data_list17 + data_list18 + data_list19 + data_list20
list_5 + data_list21 + data_list22 + data_list23 + data_list24
list_6 + data_list25 + data_list26 + data_list27 + data_list28
list_7 + data_list13 + data_list14 + data_list15 + data_list16
print('\n', list_4, '\n', list_5, '\n', list_6, '\n', list_7)
'''вариант 2'''
print('\n', list_4.data[0], list_5.data[0], list_6.data[0], list_7.data[0],'\n', list_4.data[1], list_5.data[1], list_6.data[1], list_7.data[1], '\n', list_4.data[2], list_5.data[2], list_6.data[2], list_7.data[2])
#
# for i in zip(self.data, other.data):
#     a = [x + y for x, y in zip(i[0], i[1])]
#     self.resalt.append(a)