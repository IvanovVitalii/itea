#1

class Vehicle:

    NUM_OF_WHEELS = 4
    TYPE_FUEL = 'GAS'

    def get_engine(self):
        return self._engine

    def get_fuel(self):
        return self._fuel

    def add_fuel(self, value):
        self._fuel += value
        self._weight += value

    def set_brand(self, value):
        self._brand = value

    def get_brand(self):
        return self._brand

    def get_info(self):
        return '\n'\
               f'Бренд: {self.get_brand()} ''\n'\
               f'Топливо: {self.TYPE_FUEL}''\n'\
               f'Двигатель: {self.get_engine()}'


class Car(Vehicle):

    def __init__(self, brand, engine, weight):
        self._brand = brand
        self._engine = engine
        self._weight = weight
        self._fuel = 0

    def get_weight(self):
          return f'Вес: {self._weight}, грузоподъемность: {(self._weight - self._fuel)*0.4}'


class Truck(Vehicle):

    NUM_OF_WHEELS = 8
    TYPE_FUEL = 'DIESEL'

    def __init__(self, brand, engine, weight):
        self._brand = brand
        self._engine = engine
        self._weight = weight
        self._fuel = 0

    def get_weight(self):
        return '\n'f'Вес: {self._weight}, грузоподъемность: {(self._weight - self._fuel)*0.6}'


truck = Truck('MAN', 'V8', 6000)
car = Car('BMW', 'V6', 1200)
print(car.get_brand())
print(car.TYPE_FUEL)
print(car.get_weight())
car.add_fuel(60)
print(car.get_weight())
print()
print(truck.get_brand())
print(truck.TYPE_FUEL)
print(truck.get_weight())
truck.add_fuel(500)
print(truck.get_weight())
print(car.get_info())
print(truck.get_info())