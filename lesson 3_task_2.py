try:
    def my_quest(name, surname, year_old, city, email, phone):
        print(name, surname, year_old, city, email, phone)
except ValueError:
    print('введено не число!')

my_quest(name=str(input('имя: ')), surname=str(input('фамилия: ')), year_old=int(input('год рождения: ')), city=str(input('город проживания: ')), email=str(input('email: ')), phone=int(input('телефон: ')))
