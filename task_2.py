class Road:
    def __init__(self, _length, _width, _weight, _depth):
        self.length = _length
        self.width = _width
        self.depth = _depth / 100
        self.weight = _weight
    def road_f(self):
        print('для покрытия всего дорожного полотна нужно: ' + (str(self.length * self.width * self.weight * self.depth / 10)) + 'т.')

m = Road(5000, 20, 25, 5)
m.road_f()