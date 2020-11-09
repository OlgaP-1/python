m_dict = dict()
with open(r'text6.txt', encoding='utf-8') as f:
    f.seek(0)
    lines = f.readlines()
    my_list = []
    for el in lines[0::1]:
        el = el.split()
        for i in el:
            i = i.split('(')
            if i == '-':
                continue
            i = (i[0:1])
            my_list.append(i[0:1])
    subj1 = str(my_list[0])
    subj2 = str(my_list[4:5])
    subj3 = str(my_list[8:9])
    for elem in my_list[1:2]:
        for x1 in elem:
            x1 = int(x1)
    for elem in my_list[2:3]:
        for x5 in elem:
            x5 = int(x5)
    for elem in my_list[3:4]:
        for x6 in elem:
            x6 = int(x6)
    for elem in my_list[5:6]:
        # print(elem, end=' ')
        for x2 in elem:
            x2 = int(x2)
    for elem in my_list[7:8]:
        for x3 in elem:
            x3 = int(x3)
    for elem in my_list[10:11]:
        for x4 in elem:
            x4 = int(x4)
    infor = (x1 + x5 + x6)
    fiz = x2 + x3
    fizra = x4
    m_dict.update({subj1: infor, subj2: fiz, subj3: fizra})
    print(m_dict)
