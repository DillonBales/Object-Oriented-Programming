# Name: Dillon Bales
# Date: 5/31/2025

# 1.B
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

# 2.C
from abc import ABC, abstractmethod
# 3.B
class Shape:
    @abstractmethod
    def area(self):
        pass

# 4.E (See code above)
# 5.A
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

# 6.A
# 7.A
# 8.A (See #5 Code)
# 9.C (See #5 Code)
# 10.A 
# 11.B (See #1 Code)
# 12.D
class Pet:   #upperlevel, parent, class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what I say")

class Cat(Pet): #lower level, child, class
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")
# 13.C
# 14.D
# 15.A
# 16.C
# 17.D
class Duck:
    def quack(self):
        print("Quack! Quack!")
# 18.C
# 19.B (See code above)
# 20.D
class Shape:
    @abstractmethod
    def area(self):
        pass