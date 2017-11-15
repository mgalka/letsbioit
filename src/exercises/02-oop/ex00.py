class Vehicle:
    def __init__(self, production_year, make):
        self.production_year = production_year
        self.make = make

class Car(Vehicle):
    def __init__(self, production_year, make, color):
        super().__init__(production_year, make)
        self.color = color

    def repaint(self, new_color):
        self.color = new_color


class Truck(Vehicle):
    def __init__(self, production_year, make, max_load):
        super().__init__(production_year, make)
        self.max_load = max_load


car = Car(1995, 'Opel', 'blue')
truck = Car(1996, 'Volvo', 15000)

print(car.production_year)
print(car.color)
car.repaint('pink')
print(car.color)
print(truck.make)