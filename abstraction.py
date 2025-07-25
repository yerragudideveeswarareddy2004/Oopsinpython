from abc import ABC,abstractmethod
class Vehicle:
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def drive(self):
        print("Hi this is my KIA Car")
class Bike(Car):
    def friend(self):
        print("Hi this is my discover")

obj = Bike()
obj.friend()
obj.drive()
obj.start()