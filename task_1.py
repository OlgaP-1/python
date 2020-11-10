from itertools import cycle
import time
class TrafficLight:
    __color = ['red', 'yellow', 'green']
    try:
        def running (self):
            while True:
                run = cycle(TrafficLight.get_color(self))
                print(next(run))
                time.sleep(7)
                print(next(run))
                time.sleep(2)
                print(next(run))
                time.sleep(5)
        def get_color(self):
            return self.__color
    except IndentationError:
        print('Произошла ошибка')
        exit()
    except TypeError:
        print('Произошла ошибка')
        exit()

traffic_light = TrafficLight()
traffic_light.running()
