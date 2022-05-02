import datetime
from abc import ABC, abstractmethod
from tkinter import Label, Listbox, END
from enum import Enum
from random import randint


class Animal(Enum):
    """code for each type of animal"""
    ELEPHANT = 1
    MONKEY = 2
    GIRAFFE = 3


class AnimalStatus(Enum):
    """code for each Health status"""
    ALIVE = 1
    DEAD = 2
    CAN_NOT_WALK = 3


class Zoo:
    """class for creating Zoo"""
    curr_time = datetime.datetime.now().time()

    def __init__(self, app):
        self.animals_list = [Elephant() for i in range(0, 5)]  # animal_list contains all animals in the zoo
        self.animals_list += [Monkey() for i in range(0, 5)]
        self.animals_list += [Giraffe() for i in range(0, 5)]

        self.elephant_list_box = Listbox(app, height=8, width=20)  # list of each type of animal
        self.elephant_list_box.grid(row=1, column=1)

        self.monkey_list_box = Listbox(app, height=8, width=20)  # list of each type of animal
        self.monkey_list_box.grid(row=1, column=2)

        self.giraffe_list_box = Listbox(app, height=8, width=20)  # list of each type of animal
        self.giraffe_list_box.grid(row=1, column=3)

        self.time_list_box = Listbox(app, height=1, width=20)  # list box to display cirrent time in zoo
        self.time_list_box.grid(row=7, column=2)
        self.time_list_box.insert(END, f'Zoo Current Time - {self.curr_time.strftime("%H:%M")}')

        self.show_animals()

    def show_animals(self):
        """update the current status of animals on the user interface"""
        self.elephant_list_box.delete(0, END)  # delete previous data
        self.monkey_list_box.delete(0, END) # delete previous data
        self.giraffe_list_box.delete(0, END) # delete previous data

        for ani in self.animals_list:
            if ani.animal_code == Animal.ELEPHANT.value:
                self.elephant_list_box.insert(END, (round(ani.health, 2), AnimalStatus(ani.status).name))
            elif ani.animal_code == Animal.MONKEY.value:
                self.monkey_list_box.insert(END, (round(ani.health, 2), AnimalStatus(ani.status).name))
            elif ani.animal_code == Animal.GIRAFFE.value:
                self.giraffe_list_box.insert(END, (round(ani.health, 2), AnimalStatus(ani.status).name))

    def hour_next(self):
        """called when user clicks next hour button"""
        for animal in self.animals_list:
            animal.hour_lapse(randint(0, 20))  # random number generated for each animal

        self.show_animals()
        dummy_datetime = datetime.datetime(2022, 1, 1, self.curr_time.hour, self.curr_time.minute, 0)
        dummy_datetime += datetime.timedelta(hours=1)
        self.curr_time = dummy_datetime.time()
        self.time_list_box.delete(0, END)

        self.time_list_box.insert(END, f'Zoo Current Time - {self.curr_time.strftime("%H:%M")}')  # update zoo time

    def feed(self):
        """called when user clicks feed button"""
        feed_elephant = randint(10, 25)  # random number for each type of animal
        feed_monkey = randint(10, 25)
        feed_giraffe = randint(10, 25)
        for animal in self.animals_list:
            if animal.animal_code == Animal.ELEPHANT.value:
                animal.feed(feed_elephant)
            elif animal.animal_code == Animal.MONKEY.value:
                animal.feed(feed_monkey)
            elif animal.animal_code == Animal.GIRAFFE.value:
                animal.feed(feed_giraffe)

        self.show_animals()


class AnimalBase(ABC):
    """abstract base class for animals from which all type of animals classes will be inherited"""

    @abstractmethod
    def hour_lapse(self, health_loss):
        pass

    def feed(self, feed_value):
        """method inherited by all child classes"""
        if self.status == AnimalStatus.DEAD.value:
            return

        self.health += self.health * (feed_value / 100)
        if self.health > 100:  # health connot be greater than 100
            self.health = 100

        if self.health > self.critical_health:
            self.status = AnimalStatus.ALIVE.value


class Elephant(AnimalBase):
    """inherits from AnimalBase class"""
    critical_health = 70

    def __init__(self):
        self.animal_code = Animal.ELEPHANT.value
        self.health = 100
        self.status = AnimalStatus.ALIVE.value

    def hour_lapse(self, health_loss):
        """abstract method in base class defined, to reduce health based on random number"""
        self.health -= self.health * (health_loss / 100)

        if self.health < self.critical_health:
            if self.status == AnimalStatus.ALIVE.value:
                self.status = AnimalStatus.CAN_NOT_WALK.value
            else:
                self.status = AnimalStatus.DEAD.value


class Monkey(AnimalBase):
    """inherits from AnimalBase class"""
    critical_health = 30

    def __init__(self):
        self.animal_code = Animal.MONKEY.value
        self.health = 100
        self.status = AnimalStatus.ALIVE.value

    def hour_lapse(self, health_loss):
        """abstract method in base class defined , to reduce health based on random number"""
        self.health -= self.health * (health_loss / 100)
        if self.health < self.critical_health:
            self.status = AnimalStatus.DEAD.value


class Giraffe(AnimalBase):
    """inherits from AnimalBase class"""
    critical_health = 50

    def __init__(self):
        self.animal_code = Animal.GIRAFFE.value
        self.health = 100
        self.status = AnimalStatus.ALIVE.value

    def hour_lapse(self, health_loss):
        """abstract method in base class defined, to reduce health based on random number"""
        self.health -= self.health * (health_loss / 100)
        if self.health < self.critical_health:
            self.status = AnimalStatus.DEAD.value
