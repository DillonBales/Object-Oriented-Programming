'''
Name: Dillon Bales 
Date: 5/29/2025

1.C
2.D
3.B
4.C
5.B
6.D
7.B
8.B
9.B
10.C
11.A
12.B
13.A
14.B
15.B
16.C
17.B
18.B
19.D
20.A
'''

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Car(Vehicle):
    def display_details(self):
        print(f"This car is a {self.make} {self.model}.")

class Motorcycle(Vehicle):
    def display_details(self):
        print(f"This bike is a {self.make} {self.model}.")

car1 = Car("Toyota", "Camry")
bike1 = Motorcycle("Kawasaki", "Ninja ZX-6R")

car1.display_details()
bike1.display_details()