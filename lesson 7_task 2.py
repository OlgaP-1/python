from abc import ABC, abstractmethod
class Clothes(ABC):
    def __init__(self, x):
        self.x = x
        self.y = (self.x / 6.5 + 0.5) + (self.x * 2 + 0.3)
    @abstractmethod
    def fabric_coat(self):
        pass
    @abstractmethod
    def fabric_costume(self):
        pass
class Fabric(Clothes):
    def fabric_coat(self):
        v = self.x / 6.5 + 0.5
        print(v)
    def fabric_costume(self):
        h = self.x * 2 + 0.3
        print(h)
    @property
    def sum_fabric(self):
        return f'общий расход ткани составит: {self.y} м.'
cloth = Fabric(120)
print(cloth.fabric_coat())
print(cloth.fabric_costume())
print((cloth.sum_fabric))
