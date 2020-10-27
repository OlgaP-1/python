my_dic = []
while True:
    n_1 = input('введите название: ')
    n_2 = input('введите цену: ')
    n_3 = input('введите количество: ')
    n_4 = input('введите ед.: ')
    v = {'название': n_1, 'цена': n_2, 'количество': n_3, 'eд': n_4}
    my_dic.append(v)
    v = input('хотите добавить данные? Y/N ')
    v_2 = v.lower()
    if v_2 == 'y':
        True
    else:
        m = input('хотите продолжить? ')
        if m == 'y':
            True
        else:
            for ind in enumerate(my_dic, 1):
                print(ind)
                a = my_dic[::1]
                b = {}
                my_list_1 = []
                my_list_2 = []
                my_list_3 = []
                my_list_4 = []
                my_dict_2 = {'название': my_list_1, 'цена': my_list_2, 'количество': my_list_3, 'ед': my_list_4}
                for el in a:
                    b.update(el)
                    my_list_1.append(b.get('название'))
                    my_list_2.append(b.get('цена'))
                    my_list_3.append(b.get('количество'))
                    my_list_4.append(b.get('eд'))
            for key, value in my_dict_2.items():
                print(key, ':', value)
            l = input('для возобновления ввода введите любое значение:  ')
            l_2 = l.lower()
            if l_2 == '': True
