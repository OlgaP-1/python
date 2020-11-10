class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('машина поехала'.format(self.name))

    def stop(self):
        print('машина остановилась'.format(self.name))

    def turn(self, direction):
        print('машина повернула'.format(self.name, direction))

    def show_speed(self):
        print('ваша скорость ', self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'скорость {self.name} превышена! Ваша скорость составила: {self.speed}')
        else:
            print(('ваша скорость ', self.speed))


class SportCar(Car):
    print("ваша скорость ")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'скорость {self.name} превышена! Ваша скорость составила: {self.speed}')
        else:
            print(('ваша скорость ', self.speed))


class PoliceCar(Car):
    print(f'ваша скорость ')


town = TownCar(80, 'yellow', 'ford', False)
sport = SportCar(220, 'red', 'porshe', False)
work = WorkCar(60, 'white', 'mersedes-benz', False)
polic = PoliceCar(40, 'black', 'shcoda', True)

town.show_speed()
sport.show_speed()
work.show_speed()
polic.show_speed()
