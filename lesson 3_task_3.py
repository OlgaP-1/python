def my_func(a, b, c):
    m1 = m2 = None
    for i in (a, b, c):
        if m2 is None:
            m2 = i
        elif m1 is None:
            if i > m2:
                m1, m2 = m2, i
            else:
                m1 = i
        elif i > m2:
            m1, m2 = m2, i
        elif i > m1:
            m1 = i
    return m1, m2

print(my_func(input("первое значение "), (input("второе значение ")), (input("третье значение "))))


