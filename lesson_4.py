class Human:

    height = 170
    gladness = 0

    def __init__(self, name):
        self.name = name
        self.pet = None  # Посилання на домашню тварину

    def printer(self):
        print(f'Hello, I am {self.name}, and I am a human.')

    def adopt_pet(self, pet):
        self.pet = pet
        print(f'{self.name} adopted {pet.name}!')

    def play_with_pet(self):
        if self.pet:
            self.gladness += 10
            print(f'{self.name} is playing with {self.pet.name}. Gladness increased to {self.gladness}!')
            self.pet.play()
        else:
            print(f'{self.name} has no pet to play with.')


class Student(Human):
    gladness = 30

    def printer(self):
        print(f'Hello, I am {self.name}, and I am a student.')


class Worker(Human):
    gladness = 70

    def printer(self):
        print(f'Hello, I am {self.name}, and I am a worker.')


class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.happiness = 50

    def play(self):
        self.happiness += 5
        print(f'{self.name} the {self.species} is happy! Happiness level: {self.happiness}')


nick = Worker("Nick")
kate = Student("Kate")

print(nick.height)
print(kate.height)
nick.printer()
print(nick.gladness)
print(kate.gladness)

buddy = Pet("Buddy", "dog")
nick.adopt_pet(buddy)
nick.play_with_pet()
kate.play_with_pet()  # У неї немає тварини


class Wow:

    def __wow(self):
        print('Wow')

    def _hello(self):
        print('hello')


obj = Wow()
obj._hello()
# obj.__wow()
obj._Wow__wow()


class Class1:

    var = 20

    def __init__(self):
        self.var = 10


class Class2(Class1):

    def __init__(self):
        print(self.var)
        super().__init__()
        print(self.var)
        print(super().var)


obj_1 = Class2()


class GrandParent:

    def about(self):
        print('i am grandparent')

    def about_myself(self):
        print('i am grandparent')


class Parent(GrandParent):

    def about_myself(self):
        print('i am parent')


class Child(Parent):
    def __init__(self):
        super().about()
        super().about_myself()


nick = Child()


class Computer:
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model
        self.memory = 128

    def calculate(self):
        print('calculating...')


class Display:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resolution = '4k'

    def display(self):
        print('i display an image')


class SmartPhone(Computer, Display):
    def __init__(self, model):
        super().__init__(model)

    def print_info(self):
        print(self.memory)
        print(self.resolution)
        print(self.model)


phone = SmartPhone(model='super max pro 10')
phone.print_info()
