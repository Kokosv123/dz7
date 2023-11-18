import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
        self.day = 0

    def to_study(self):
        self.progress += 0.12
        self.gladness -= 5

    def to_sleep(self):
        self.gladness += 3

    def to_chill(self):
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            self.alive = False
        elif self.gladness <= 0:
            self.alive = False
        elif self.progress > 5:
            self.alive = False

    def end_of_day(self):
        print(f"============== Day {self.day} of {self.name}'s life ==============")
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")

    def live_one_day(self):
        self.day += 1
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.is_alive()
        self.end_of_day()

    def __iter__(self):
        return self

    def __next__(self):
        if not self.alive or self.day >= 365:
            raise StopIteration
        self.live_one_day()
        return self.day, self.progress, self.gladness

nick = Student(name="Nick")
for day, progress, gladness in nick:

    pass
