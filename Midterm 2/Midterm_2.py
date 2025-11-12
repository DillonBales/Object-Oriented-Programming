# Dillon Bales 
# 6/14/2025

#Question 1
from abc import ABC, abstractmethod 

class Device(ABC):

    @abstractmethod
    def show_info(self):
        pass


class Phone(Device):
    def __init__(self, brand):
        self.brand = brand
        
    def show_info(self):
        print(f"This phone is a(n) {self.brand} device")
        

class Tablet(Device):
    def __init__(self, brand):
        self.brand = brand
        
    def show_info(self):
        print(f"This tablet is a(n) {self.brand} device")

class Laptop(Device):
    def __init__(self, brand):
        self.brand = brand
        
    def show_info(self):
        print(f"This laptop is a(n) {self.brand} device")



phone_brand = input("What is the phone brand: ")
tablet_brand = input("What is the tablet brand: ")
laptop_brand = input("What is the laptop brand: ")

phone1 = Phone(phone_brand)
tablet1 = Tablet(tablet_brand)
laptop1 = Laptop(laptop_brand)

phone1.show_info()
tablet1.show_info()
laptop1.show_info()

#Question 2

class Book:

    books = []

    def __init__(self, title, author, ISBNs):
        self.title = title
        self.author = author
        self.ISBNs = ISBNs
        Book.books.append(self)

    def display_info(self):
        print(f"This is {self.title} by {self.author} and its ISBN is {self.ISBNs}")

    @classmethod
    def search_by_author(cls, author):
        return [book for book in cls.books if book.author.lower() == author.lower()]
    
book1 = Book("1984", "George Orwell", "1234567890")
book2 = Book("Animal Farm", "George Orwell", "0987654321")
book3 = Book("To Kill a Mockingbird", "Harper Lee", "1122334455")

book1.display_info()
book2.display_info()
book3.display_info()

search_author = input("Enter author name: ")
found = Book.search_by_author(search_author)


if found:
    for book in found:
        book.display_info()
else:
    print("Nothing found")

#Question 3

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        print(self.base * self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius= radius        
    
    def area(self):
        print((self.radius ** 2) * 3.14)

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height    
    
    def area(self):
        print((self.base * self.height) / 2)
    
rectangle = Rectangle(2,4)
triangle = Triangle(2,4)
circle = Circle(3)

rectangle.area()
triangle.area()
circle.area()

#Question 4

class ImageAlbum:
    images = []  # Shared list for all image instances

    def __init__(self, size_length, size_height, coordinate_x=0, coordinate_y=0):
        self.size_length = size_length
        self.size_height = size_height
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        ImageAlbum.images.append(self)

    @classmethod
    def arrange_images(cls):
        current_x = 0
        for img in cls.images:
            img.coordinate_x = current_x
            img.coordinate_y = 0  
            current_x += img.size_length  

    @classmethod
    def print_image_coordinates(cls):
        for img in cls.images:
            print(f"({img.coordinate_x}, {img.coordinate_y})")


photo1 = ImageAlbum(20, 20)
photo2 = ImageAlbum(10, 10)
photo3 = ImageAlbum(5, 5)

ImageAlbum.arrange_images()
ImageAlbum.print_image_coordinates()
 
#Question 5

class Duck:
    def quack(self):
        print("Quack! Quack!")

class Person:
    def quack(self):
        print("I can't quack, but I can mimic!")

def check_quack_behavior(obj):
    try: 
        obj.quack()
    except AttributeError:
        print("This object doesn't quack!")

duck = Duck()
person = Person()
train = "train"

check_quack_behavior(duck)
check_quack_behavior(person)
check_quack_behavior(train)
            