proceeds = int(input('Введите сумму выручки: '))
costs = int(input('Введите сумму издержек: '))
profit = proceeds - costs
profitability = proceeds / costs

if proceeds > costs:
    print('Вы работаете в прибыль')
    print('Ваша прибыль составила ' + str(profit))
    print('рентабельность компании составляет ' + '{:.2f}'.format(profitability))
    question = int(input('Введите число сотрудников компании '))
    profit_employee = profit / question
    print('Прибыль компании в расчете на одного сотрудника составляет ' + str(profit_employee))
else:
    print('Вы работаете в убыток')
    print('ваша прибыль составила ' + str(profit))