from math import factorial
from itertools import count

n = int(input('введи число: '))
a = factorial(n)
print(a)
def generator():
    for el in count(1):
        yield factorial(el)

x = 1
for i in generator():
    print('Factorial {} - {}'.format(x, i))
    if x == n:
        break
    x += 1

