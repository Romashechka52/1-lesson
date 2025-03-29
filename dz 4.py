class Engine:
    def __init__(self, power):
        self.power = power

    def start_engine(self):
        return f"Engine with {self.power} HP started."


class Wheels:
    def __init__(self, wheel_count):
        self.wheel_count = wheel_count

    def rotate_wheels(self):
        return f"Rotating {self.wheel_count} wheels."


class CarBody:
    def __init__(self, color):
        self.color = color

    def paint_car(self, new_color):
        self.color = new_color
        return f"Car painted {new_color}."


class Car(Engine, Wheels, CarBody):
    def __init__(self, power, wheel_count, color, brand):
        Engine.__init__(self, power)
        Wheels.__init__(self, wheel_count)
        CarBody.__init__(self, color)
        self.brand = brand

    def car_info(self):
        return (f"Brand: {self.brand}, Power: {self.power} HP, Wheels: {self.wheel_count}, "
                f"Color: {self.color}.")



my_car = Car(power=560, wheel_count=4, color="Red", brand="ferrari")
print(my_car.start_engine())
print(my_car.rotate_wheels())
print(my_car.paint_car("Blue"))
print(my_car.car_info())
