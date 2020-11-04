''' 1 вариант'''
import random
list = []
while len(list) != 5:
    x = random.randint(5, 21)
    list.append(x)
print(list)

'''2 вариант '''
from itertools import count
my_list1 = []
for el in count(3, 1):
    if el > 10:
        break
    else:
        my_list1.append(el)
print(my_list1)

'''3 вариант '''
from itertools import cycle

my_list_2 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = cycle(my_list_2)
i = 0
while i != 10:
    print(next(new_list))
    i += 1