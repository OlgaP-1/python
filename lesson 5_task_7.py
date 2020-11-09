import json
my_list = []
dic_firm = dict()
dic_loss = dict()
dic_average = dict()
list_data = []
with open('text_7.txt', encoding='utf-8') as f:
    f.seek(0)
    lines = f.readlines()
    for el in lines:
        el = el.split()
        profit = int(el[2]) - int(el[3])
        dic_firm[el[0]] = el[2]

        if profit > 0:
            my_list.append(el[2])
        if profit < 0:
            # print(el)
            dic_loss[el[0]] = profit
        # print(el[0])

        for i1 in my_list[0:1]:
            i1 = int(i1)
        for i2 in my_list[1:2]:
            i2 = int(i2)

    sum_i = i1 + i2
    average_profit = sum_i / len(my_list)
    dic_average['average_profit:'] = average_profit
    # print(average_profit)
    print(dic_firm)
    print(dic_loss)
    print(dic_average)
    list_data.append((dic_firm, dic_average, dic_loss))
    print(list_data)
with open('text_7.txt', 'w') as write_f:
    json.dump(list_data, write_f)
with open('text_7.json') as read_f:
    list_data = json.load(read_f)
print(list_data)
print(type(list_data))
    # a = sum([range(0, len(my_list))])
    # sum = 0
    # for element in my_list:
    #     sum = sum + element + element

    # print(i2)

# print(sum([profit]))
            # average_profit = (sum([int(el[2])]))
            # print(average_profit)

# / len(el[2])


#
# firm_dict = {}
# average_profit = []
# with open('text_7.txt') as f:
#     lines = f.readlines()
#     for line in lines:
#         name, form, revenue, costs = line.split()
#         profit = int(revenue) - int(costs)
#         firm_dict[name] = profit
#         if profit > 0:
#             average_profit.append(profit)
#
# average_profit = sum(average_profit) / len(average_profit)
# out_info = [firm_dict, {'average_profit ": average_profit'}]
#
# with open('7.json' ',' 'w') as f_json:
#     json.dump(out_info, f_json)
#
# with open('7.json') as f_json:
#     print(json.load(f_json))