
class Human:

    height = 170
    gladness = 0

    def printer(self):
        print('hello im human')


class Student(Human):
    gladness = 30

    def printer(self):
        print('hello im student')


class Worker(Human):
    gladness = 70
    def printer(self):
        print('hello im worker')


nick = Worker()
kate = Student()
print(nick.height)
print(kate.height)
nick.printer()
print(nick.gladness)
print(nick.gladness)


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


class SmartPhone(Computer, Display):  # Змінили порядок успадкування
    def __init__(self, model):
        super().__init__(model)  # Передаємо model у Computer.__init__()

    def print_info(self):
        print(self.memory)
        print(self.resolution)
        print(self.model)


phone = SmartPhone(model='super max pro 10')
phone.print_info()

