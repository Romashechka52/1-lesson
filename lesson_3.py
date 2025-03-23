import random

class Human:
    def __init__(self, name='Human', job=None, car=None, home=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        self.home = House()
        print(f"{self.name} отримав будинок")

    def get_car(self):
        self.car = Auto(brands_of_car)
        print(f"{self.name} отримав автомобіль {self.car.brand}")

    def get_job(self):
        self.job = Job(job_list)
        print(f"{self.name} отримав роботу: {self.job.job} з зарплатою {self.job.salary}")

    def eat(self):
        if self.home.food > 0:
            self.satiety += 10
            self.home.food -= 10
            print(f"{self.name} поїв")
        else:
            print("Немає їжі! Потрібно купити")

    def work(self):
        if self.job:
            self.money += self.job.salary
            self.gladness -= self.job.gladness_less
            self.satiety -= 5
            print(f"{self.name} працював і заробив {self.job.salary}")

    def shopping(self):
        if self.money >= 50:
            self.home.food += 50
            self.money -= 50
            print(f"{self.name} купив їжу")
        else:
            print("Недостатньо грошей")

    def chill(self):
        self.gladness += 10
        self.satiety -= 5
        print(f"{self.name} відпочив")

    def clean_home(self):
        if self.home:
            self.home.mess = 0
            self.gladness -= 5
            print(f"{self.name} прибрав у будинку")

    def to_repair(self):
        if self.car:
            self.car.strength = 100
            self.money -= 50
            print(f"{self.name} відремонтував авто")

    def days_indexes(self, day):
        print(f"День {day}: {self.name}")
        print(f"Гроші: {self.money}")
        print(f"Щастя: {self.gladness}")
        print(f"Ситість: {self.satiety}")
        print(f"Їжа в домі: {self.home.food}")

    def is_alive(self):
        if self.satiety <= 0:
            print(f"{self.name} помер від голоду")
            return False
        if self.gladness <= 0:
            print(f"{self.name} впав у депресію")
            return False
        return True

    def live(self, day):
        if not self.home:
            self.get_home()
        if not self.car:
            self.get_car()
        if not self.job:
            self.get_job()

        self.days_indexes(day)
        cube = random.randint(1, 6)
        if cube == 1:
            self.work()
        elif cube == 2:
            self.eat()
        elif cube == 3:
            self.shopping()
        elif cube == 4:
            self.chill()
        elif cube == 5:
            self.clean_home()
        elif cube == 6:
            self.to_repair()
        return self.is_alive()

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print('Автомобіль не може рухатися')
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']

brands_of_car = {
    'BMW': {'fuel': 100, 'strength': 100, 'consumption': 7},
}

job_list = {
    'Python developer': {'salary': 40, 'gladness_less': 3},
}

nick = Human('Nick')
for day in range(1, 8):
    if not nick.live(day):
        break
