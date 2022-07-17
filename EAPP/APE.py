# Basics ..

from classes import *
from classes import Car
import module as m
from module import *  # * means everything
import time
import random
import os
import shutil

seperator = '------------------------'

# variables

print(seperator)

x = str(12)

print("Alex is ", x)

# for function = does an operation for an i amount of time

print(seperator)

for i in 'Alex':
    print(i, end="")

print("\n")

for seconds in range(10, 0, -1):
    # this will only print from 10~1
    print(seconds, end=' ')
    if seconds == 1:
        time.sleep(1)
        print('command ended')

# SYMBOL PRINTER

print(seperator)

height = int(input('Enter height:'))
width = int(input("Enter a width:"))
symbol = input("Enter a symbol to use:")

print(seperator)

for i in range(height):
    for j in range(width):
        print(symbol, end="")

    print('')

# CODES
# break = stops the code
# for instance if name != "": break

# continue basically skips to the next command
# for instance if i == "-": continue

# pass does nothing,absolutely nothing
# if num == 13: pass

# LISTS

print(seperator)

body_parts = ["head", "nose", "wee-wee"]
# body_parts

body_parts.append("icecream")
# adds icecream

body_parts.remove("nose")
# removes

body_parts.pop()
# removes the last value in the list

body_parts.insert(0, "bum")
# adds something in a specific index

body_parts.sort()
# sorts in in the alphabetical order

# lastly x.clear removes everything

print(body_parts)

# 2D LISTS

print(seperator)

boomer = [50, "old", "boomery"]
teen = [18, "young", "savagey"]
toddler = [2, "very young", "cute"]

ages = [boomer, teen, toddler]

print(ages[0][0])
# This will print 0 of ages' 0

# tuple = collection of datas that are related to each other

print(seperator)

student = ("Alex", 2010, "male")

print('There is only', student.count("Alex"), 'Alex in the student tuple.')
# finds how many 'Alex' are in the student tuple

print('2010, the birth year of Alex is located on index ', student.index(2010))
# finds in what index 2010 is in

for x in student:
    if x == "male":
        print('male')
        break
    print(str(x) + ",ㅤ", end="") # Example: str(x) = Alex + , = Alex,(space)

print('\n')

if "male" in student:
    print("The student is a male.")

# set = a list which is not in order,and has no index,no duplicate values

print(seperator)

tech = {"computer", "tv", "game_consol"}
mobile_tech = {"tablet", "phone", "player"}

tech.add("smart_watch")
# adds
tech.remove("game_consol")
# removes
# tech.clear() would delete everything
tech.update(mobile_tech)
# adds another list in the list
# you can also use x.union(y)
# there is also x.Difference(y)

for i in tech:
    print(str(i) + "ㅤ", end="")

print()

# dictionary = a set with special keys

print(seperator)

Capitals = {"Usa": "Washington DC",
            "Russia": "Moscow",
            "China": "Beijing"}

print(Capitals["Russia"])
# This will print the capital of Russia
print(Capitals.get("Germany"))
# this will print none,since there is no Germany in Capitals, if there were, it shouldve just printed Berlin
print(Capitals.keys())
# prints the countries, not the capitals
print(Capitals.values())
# prints the capitals, not the countries
print(Capitals.items())
# prints everything
Capitals.update({"Germany": "Munich"})
# adds Germany and Munich as it's capital 
Capitals.update({"Germany": "Berlin"})
# updates Germany's value
Capitals.pop("China")
# removes China out
# Capitals.clear would result in deletion of everything
for key, values in Capitals.items():
    print(key, values)

# index opreator [] = gives access to a sequence's str,list,tuples

print(seperator)

name = "alex Kim#"
if name[0].islower():
    name = name.capitalize()
# this will capitalize the 0 index

first_name = name[:4].upper()
# makes characters from 0-3 upper
last_name = name[5:].lower()
# make characters from 4:end lower
last_character = name[-1].removeprefix
# accesses the last integer
print(name + 'Your names are ', first_name, "&", last_name)

# functions & return statements
 
print(seperator)


def multiply(a, b):
    return a * b


mul = multiply(6, 7)

print(mul)

# keyboard argument

print(seperator)


def helloAlex(fname, who, lname):
    print("Hi " + fname + " " + who + " " + lname)


helloAlex(lname="Pizzaz", fname="Zack", who="Zuzzezo")

# nested function calls = function calls inside other function calls

print(seperator)

print('A positive whole number of this would be', round(abs(float(input("Enter a negative decimal:")))))

# scopes = The region that a variable can be global and local

pooo = "POO"


def PrintPoo():
    pooo = "POO"  # pooo variable can only be used inside of the function
    print(pooo)


# If I were to delete the local pooo, than the print(poo) would print the global poo

# args = paramter that will pack all arguments into a tuple useful so that a function can accept a varying amount of arg
#        uments and can be named however you want

print(seperator)


def add(*args):
    sum = 0
    args = list(args)
    args[0] = 0
    for i in args:
        sum += i
    return sum


print(add(1, 2, 3, 4, 5, 6))

# kwargs = paramter that will pack all arguments into a dictionary useful so that a function can accept a varying amount of
#          arguments and can be named however you want

print(seperator)


def HelloWorld(**kwargs):
    """print("Hello "+kwargs["First"]+" "+kwargs["Middle"]+kwargs["Last"])"""
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")
    # more efficient and smart


HelloWorld(First="Alex ", Middle="", Last="Kim")

# str.format() = optional method that gives users more control when displaying an output

print(seperator)

animal = "cow"
item = "moon"
# print("The"+animal+"jumped over the"+item)

print("\nThe {cow} jumped over the {0}".format(item, cow="cow"))

text = "The {} jumped over the {}"

text.format(animal, item)

print(text)

alex = "Alex"

print("Hello, my name is {:10}. Nice to meet you ".format(alex))

print("Hello, my name is {:^10}. Nice to meet you ".format(alex))

pi = 3.14159
number = 1000

print("The number pi is {:.2f}".format(pi))
# {:.2f} is the variable pi but only shows decimals till the tenth
print("The number is {:,}".format(number))
# this will print 1,000
print("The number is {:b}".format(number))
# this will print the binary value
print("The number is {:o}".format(number))
# this will print the octal value
print("The number is {:X}".format(number))
# this will print the hexadecimal
print("The number is {:E}".format(number))
# This will print the scientific notation

# random

dice = random.randint(1, 6)
print(dice)

randomlist = ['rock', 'paper', 'scissors']
randomlist = random.choice(randomlist)
print(seperator)
print(randomlist)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
print(seperator)
random.shuffle(cards)
# This will randomize the order of the cards
print(cards)

# exception = event detected during execution that interrupt the flow of a program

print(seperator)

try:
    numerator = int(input('Enter a number to divide:'))
    denominator = int(input('Enter a denominator:'))
    result = numerator / denominator
except ZeroDivisionError as ZERORULE:
    print('You can\'t divide by zero you idiot!')
except ValueError as NOTANUM:
    print('Enter a number plz')
except Exception:
    print('Something went wrong :(')
else:
    print(result)
finally:
    print('This will always execute.')

# files

print(seperator)

a_path = 'C:\\Users\\user\\Desktop\\code.txt.txt'

if os.path.exists(a_path):
    print('That location exists!')
    if os.path.isfile(a_path):
        print('This path is a file')
        # this will see if this path is a file
    elif os.path.isdir(a_path):
        print('That is a directory.')
        # this will find out if the path is a directory/folder
else:
    print('That location does not exist!')

# file(how to read it)

print(seperator)

try:
    with open('text.txt',
              'r') as file:  # if this were tto be in your computer file you should add the location in the parenthesis
        print(file.read())
        # the withopen function will automatically close the function, meaning that you will have to call the
        # withopen function again in order to edit it after you are done with the function
except FileNotFoundError:
    print('The file is not found :(')

# file(how to write it)

print(seperator)

text = 'Python is very cool '

with open('text.txt', 'w') as file:
    file.write(text)

with open('text.txt', 'a') as file:
    file.write(text)

# file(how to copy it)

# copyfile() = copies content of a file
# copy() =     copyfile() + permission mode + destination can be a directory
# copy2() =    copy() + copies metadata ( file's creation and modification times)


shutil.copyfile('text.txt', 'copy.txt'
                # If you do not put a file location, also, because the name is not modified,the file is not
                # reduplicated, it will be located in the python file
                )  # there are two arguments, src[original] and dst[new]

# file(how to move it)

source = 'test.txt'
destination = 'C:\\Users\\user\\Desktop\\Junho\\Coding\\Python\\test.txt'

try:
    if os.path.exists(destination):
        print('There is already a file there')
    else:
        os.replace(source, destination)
        print(source + ' was moved')
except FileNotFoundError:
    print(source + ' was not found.')

# file(how to delete it)

path = 'Text Folder'  # Instead use Text Folder/test.txt

# this program cannot delete empty folders
try:
    # os.remove(path)
    # shutil.rmtree(path) consider this file as dangerous since it deletes the folder and all of its files
    os.rmdir(path)  # this will result in an os error since the folder contains files, if it did not, it would work
except FileNotFoundError:
    print('{}was not found'.format(path))
except PermissionError:
    print('You do not hav the permission to delete {}'.format(path))
except OSError:
    print('you cannot delete that file since it contains a file')
else:
    print(path + 'was deleted')

# module = a file containing python code.May contain functions, classes, etc


# used with modular programming, which is to separate program into parts
print(seperator)
print()

m.hello()

m.bye()

hello()

bye()

print()

# help('module will show you all the modules in python)

# classes

print(seperator)

car_1 = Car('Ferrari', 'GTC4 Lusso', 2022, 'Red')  # DISCLAIMER: Car_1 and Car will both use .(for instance)drive

motorbike = Car('Dodge', 'Tomahawk', 2003, 'Grey')

motorbike.wheels = 2

print(car_1.make)
print(motorbike.make)

car_1.drive()

motorbike.stop()

print(Car.wheels)  # This will display the motorbike's, and the car's number of wheels

# method chaining

print(seperator)

Car.drive().stop()


# super() = Function used to give access to the methods of a parent class.
#           Returns a temporary object of a parent class when used




Square.area()
Cube.volume()

# abstract class = a class which contains one or more abstract methods
# abstract method = a method that has a declaration but does not have an implementation

print(seperator)

vehicle = Vehicle()
vehicle.drive