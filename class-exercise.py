from abc import ABC, abstractmethod

#################################################################
# Basic example:


class Language:
    def __init__(self, lang) -> None:
        self.lang = lang
    me = 'Language Class'

    def message(self):
        print("this is "+self.lang+", nice to meet you " + self.me)


languages = [Language("python"), Language("javascript")]

# for language in languages:
#     language.message()

#################################################################
# Abstract Base Classes


class Vehicle(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def go_forward(self):
        print("this is from ABC")


class Car(Vehicle):
    def __init__(self):
        super().__init__()

    def go_forward(self):
        return super().go_forward()


class Truck(Vehicle):
    def __init__(self):
        super().__init__()

    def go_forward(self):
        print("this is a truck moving forward")

# vehicle1 = Vehicle()


car1 = Car()
car1.go_forward()

truck1 = Truck()
truck1.go_forward()

#################################################################
# magic method __dict__

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(list(enumerate(lst)))
# for i, value in enumerate(lst):
#     print(lst)
#     if i % 2 == 0:
#         lst.pop(i)

for i in range(len(lst)):
    print(lst)
    if i % 2 == 0:
        lst.pop(i)

print(lst)
