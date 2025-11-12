# Name: Dillon Bales
# Date: 5/31/2025

# 1. Shape Area Calculation (Using Abstract Base Classes)
from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width        

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
        
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height) / 2

shapes = [Rectangle(2, 4), Circle(4), Triangle(2, 3)]

for shape in shapes:
    print(shape.area())

# 2. Vector Addition (Using Operator Overloading)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, second):
        return Vector(self.x + second.x, self.y + second.y)
    
v1 = Vector(1, 3)
v2 = Vector(2, 4)
v3 = v1 + v2 

print(v3.x, v3.y)

# 3. Animal Sounds (Using Method Overriding)

class Animal:
    def make_sound(self):
        print("a generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

class Duck(Animal):
    def make_sound(self):
        print("Quack")


def make_animal_sound(animal):
    animal.make_sound()

dog1 = Dog()
cat1 = Cat()
duck1 = Duck()

make_animal_sound(dog1)
make_animal_sound(cat1)
make_animal_sound(duck1)

# 4. Dynamic Typing: Duck or Not?

class Duck:
    def quack(self):
        print("Quack! Quack!")

class Person:
    def quack(self):
        print( "I can't quack, but I can mimic!")

def check_quack_behavior(obj):
    try: 
        obj.quack()
    except AttributeError:
        print("This object doesn't quack!")

duck = Duck()
person = Person()
car = "I am a car"

check_quack_behavior(duck)
check_quack_behavior(person)
check_quack_behavior(car)