import datetime
from abc import ABC,abstractmethod
from tkinter import Label, Listbox,END
from enum import Enum
from random import randint


class Animal(Enum):
    ELEPHANT = 1
    MONKEY = 2
    GIRAFFE = 3


class AnimalStatus(Enum):
    ALIVE = 1
    DEAD = 2
    CAN_NOT_WALK = 3


class Zoo:
    curr_time = datetime.datetime.now().time()

    def __init__(self,app):
        self.animals_list = [Elephant() for i in range(0,5)]
        self.animals_list += [Monkey() for i in range(0,5)]
        self.animals_list += [Giraffe() for i in range(0,5)]

        self.elephant_list_box = Listbox(app, height=8, width=20)
        self.elephant_list_box.grid(row=1, column=1)

        self.monkey_list_box = Listbox(app, height=8, width=20)
        self.monkey_list_box.grid(row=1, column=2)

        self.giraffe_list_box = Listbox(app, height=8, width=20)
        self.giraffe_list_box.grid(row=1, column=3)

        self.time_list_box = Listbox(app, height=1, width=20)
        self.time_list_box.grid(row=7,column=2)
        self.time_list_box.insert(END,f'Zoo Current Time - {self.curr_time.strftime("%H:%M")}')

        self.show_animals()



    def show_animals(self):
        self.elephant_list_box.delete(0,END)
        self.monkey_list_box.delete(0,END)
        self.giraffe_list_box.delete(0,END)

        for ani in self.animals_list:
            if ani.animal_code == Animal.ELEPHANT.value:
                self.elephant_list_box.insert(END, (round(ani.health,2), AnimalStatus(ani.status).name))
            elif ani.animal_code == Animal.MONKEY.value:
                self.monkey_list_box.insert(END, (round(ani.health,2), AnimalStatus(ani.status).name))
            elif ani.animal_code == Animal.GIRAFFE.value:
                self.giraffe_list_box.insert(END, (round(ani.health,2), AnimalStatus(ani.status).name))

    def hour_next(self):
        for animal in self.animals_list:
            animal.hour_lapse(randint(0,20))

        self.show_animals()
        dummy_datetime = datetime.datetime(2022,1,1,self.curr_time.hour,self.curr_time.minute,0)
        dummy_datetime += datetime.timedelta(hours=1)
        self.curr_time = dummy_datetime.time()
        self.time_list_box.delete(0,END)

        self.time_list_box.insert(END, f'Zoo Current Time - {self.curr_time.strftime("%H:%M")}')


    def feed(self):
        feed_elephant = randint(10,25)
        feed_monkey = randint(10,25)
        feed_giraffe = randint(10,25)
        for animal in self.animals_list:
            if animal.animal_code == Animal.ELEPHANT.value:
                animal.feed(feed_elephant)
            elif animal.animal_code == Animal.MONKEY.value:
                animal.feed(feed_monkey)
            elif animal.animal_code == Animal.GIRAFFE.value:
                animal.feed(feed_giraffe)

        self.show_animals()


class AnimalBase(ABC):

    @abstractmethod
    def hour_lapse(self,health_loss):
        pass

    def feed(self,feed_value):
        if self.status == AnimalStatus.DEAD.value:
            return

        self.health += self.health * (feed_value / 100)
        if self.health > 100:
            self.health = 100

        if self.health > self.critical_health:
            self.status = AnimalStatus.ALIVE.value


class Elephant(AnimalBase):
    critical_health = 70

    def __init__(self):
        self.animal_code = Animal.ELEPHANT.value
        self.health = 100
        self.status = AnimalStatus.ALIVE.value

    def hour_lapse(self,health_loss):
        self.health -= self.health * (health_loss / 100)

        if self.health < self.critical_health:
            if self.status == AnimalStatus.ALIVE.value:
                self.status = AnimalStatus.CAN_NOT_WALK.value
            else:
                self.status = AnimalStatus.DEAD.value


class Monkey(AnimalBase):
    critical_health = 30

    def __init__(self):
        self.animal_code = Animal.MONKEY.value
        self.health = 100
        self.status = AnimalStatus.ALIVE.value

    def hour_lapse(self,health_loss):
        self.health -= self.health * (health_loss / 100)
        if self.health < self.critical_health:
            self.status = AnimalStatus.DEAD.value


class Giraffe(AnimalBase):
    critical_health = 50

    def __init__(self):
        self.animal_code = Animal.GIRAFFE.value
        self.health = 100
        self.status = AnimalStatus.ALIVE.value

    def hour_lapse(self,health_loss):
        self.health -= self.health * (health_loss / 100)
        if self.health < self.critical_health:
            self.status = AnimalStatus.DEAD.value