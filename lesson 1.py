#
# class Student:
#
#    amount_of_students = 0
#
#    def __init__(self, name,  height=160):
#        self.name = name
#        self.height = height
#        Student.amount_of_students += 1
#
#    def grow(self, value=1):
#            self.height += value
#
#    def __str__(self):
#        return f'i am Student, My name is {self.name}'
#
#
# Nick = Student(name='Nick')
# print(Nick.height)
# Nick.grow(25)
# print(Nick.name,  Nick.height)
# print(Nick)
#
# Kate = Student(name='Kate', height=170)
# print(Kate.height)
#
# print(Nick.amount_of_students)
# print(Student.amount_of_students)



import random


class Student:

    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
            print('time to study...')
            self.progress += 0.12
            self.gladness -= 5

    def to_sleep(self):
        print('i will seep')
        self.gladness += 3

    def to_chill(self):
        print('Rest time')
        self.progress -= 0.1
        self.gladness += 5

    def is_alive(self):
        if self.progress < -0.5:
            print('failed...')
            self.alive = False
        elif self.gladness <= 0:
            print('depression..')
            self.alive = False
        elif self.progress > 5:
            print('genius..')
            self.alive = False

    def end_of_day(self):
        print(f'Gladness - {self.gladness}')
        print(f'Progress - {self.gladness}')

    def live(self, day):
        print(f'Day {day} of {self.name} life')
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        else:
            self.to_chill()

            self.end_of_day()
            self.is_alive()


nick = Student(name='Nick')
for day in range (366):
    if nick.alive == False:
        break
    nick.live(day)