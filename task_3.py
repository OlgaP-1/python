# class Worker:
#     name = 'Сергей'
#     surname = 'Петров'
#     position = 'Руководитель'
#     _income = {"wage": 200000, "bonus": 60000}
#     class Position:
#         def get_full_name(self):
#             x = Worker.name + ' ' + Worker.surname + ' ' + Worker.position + ' '
#             return x
#         def get_total_income(self):
#             s = Worker._income
#             s = sum(s.values())
#             return s
# a = Worker.Position ()
# print(a.get_full_name(), a.get_total_income())
"""2 вариант"""
class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income
class Position(Worker):
    def get_full_name(self):
        x = self.name + ' ' + self.surname + ' ' + self.position + ' '
        return x
    def get_total_income(self):
        s = self._income
        s = sum(s.values())
        return s
p = Position('Сергей', 'Петров', 'Руководитель', {"wage": 200000, "bonus": 60000})
print(p.get_full_name())
print(p.get_total_income())