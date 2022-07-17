from abc import *

class Vehicle:
    @abstractmethod
    def drive(self):
        pass
     
class Car(Vehicle):
    wheels = 4  # class variable

    def __init__(self, make, model, year, color):
        self.make = make  # instance variable  #The self keyword allows you to manipulate
        self.model = model  # instance variable  #the method temporarily, for instance car_1 =
        self.year = year  # instance variable  #Car(make, model, year, color)
        self.color = color  # instance variable

    def drive(self):
        print('This', self.make, self.model, 'is driving.')
        return self

    def stop(self):
        print('This', self.make, self.model, 'has stopped.')
        return self


class Animal:
    alive = True  # Since this is a class variable, when another class inherits it, it inherits the alive variable

    def eat(self):
        print('This animal is eating')

    def sleep(self):
        print('This animal is sleeping')


class Rabbit(Animal):
    def eat(self):
        print('This rabbit is eating grass')

    def run(self):
        print('This rabbit is running')


class Fish(Animal):

    def swim(self):
        print('This fish can swim')


class Hawk(Animal):

    def fly(self):
        print('This Hawk can fly')


rabbit = Rabbit()

# This class is multiple inheritance and a multilevel inheritance class, since it inheritmore than one class, 
# one which inherits from another
                             
class Salmon(Fish):  

    def tasty(self):
        print('This Salmon is tasty')


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Rectangle):

    def __init__(self, length, width):
        super().__init__(length, width)
        '''    def __init__(self, length, width):
               self.length = length
               self.width = width    '''

    def area(self):
        return self.length * self.width


class Cube(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
        '''    def __init__(self, length, width, height):
               self.length = length
               self.width = width
               self.height = height    '''


    def volume(self):
        return self.length * self.width * self.height
