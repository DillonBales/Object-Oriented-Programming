#Dillon Bales
#5/16/2025

#Problem 1
class Book:
    genre = "Fiction"

    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def change_genre(cls, newGenre):
        cls.genre = newGenre
    
    def display_books(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {Book.genre} \n")

book1 = Book("The Night Circus", "Erin Morgenstern")
book2 = Book("The Martian", "Andy Weir")
book3 = Book("Circe", "Madeline Miller")

book1.display_books()
book2.display_books()
book3.display_books()

print("Changing genre ...\n")
Book.change_genre("Fantasy")

book1.display_books()
book2.display_books()
book3.display_books()

#Problem 2
class Rectangle:
    
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        return area

    @classmethod
    def create_square(cls):
        length = 5
        width = 5
        area = length * width
        return area
        


rectangle1 = Rectangle(4, 2)
rectangle2 = Rectangle(3, 5)
rectangle3= Rectangle(6, 8)

print(rectangle1.calculate_area())
print(rectangle2.calculate_area())
print(rectangle3.calculate_area())
print(f"{Rectangle.create_square()}\n")

# Problem 3
class TempuratureConverter:
    @staticmethod
    def celcius_to_fahrenheit(cel_temp):
        fahr_temp = (cel_temp * (9/5)) + 32
        print(fahr_temp)
    
    @staticmethod 
    def fahrenheit_to_celcius(fahr_temp):
        cel_temp = (fahr_temp - 32) * (5/9)
        print(f"{cel_temp} \n")
    
TempuratureConverter.celcius_to_fahrenheit(30)
TempuratureConverter.fahrenheit_to_celcius(32)

#Problem 4
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"I make this sound: {self.sound}\n")


class Dog(Animal):
    def __init__(self, name, sound, breed):
        super().__init__(name, sound)
        self.breed = breed

    def make_sound(self):
        print(f"I make this sound: {self.sound}")
        print(f"I am a {self.breed}\n")


class Cat(Animal):
    def __init__(self, name, sound, fur_color):
        super().__init__(name, sound)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"I make this sound: {self.sound}")
        print(f"My fur is {self.fur_color}\n")

animal1 = Dog("Arthur", "Woof", "Pitbull")
animal2 = Cat("Merlin", "Meow", "Black")

animal1.make_sound()
animal2.make_sound()

        
