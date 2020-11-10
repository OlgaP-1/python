class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки.')
class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой.')
class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашем.')
class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером.')

pen = Pen('j')
pencil = Pencil('gg')
handle = Handle('gg')
pen.draw()
pencil.draw()
handle.draw()