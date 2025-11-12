# Dillon Bales 
# 6/24/2025

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
        print(f"This phone is a(n) {self.brand} device. It is the smallest and most convenient device.")
        

class Tablet(Device):
    def __init__(self, brand):
        self.brand = brand
        
    def show_info(self):
        print(f"This tablet is a(n) {self.brand} device. It has a larger screen than a phone, making it easier to use")

class Laptop(Device):
    def __init__(self, brand):
        self.brand = brand
        
    def show_info(self):
        print(f"This laptop is a(n) {self.brand} device. It has much more computing power than a phone or tablet.")



phone_brand = input("What is the phone brand: ")
tablet_brand = input("What is the tablet brand: ")
laptop_brand = input("What is the laptop brand: ")

phone = Phone(phone_brand)
tablet = Tablet(tablet_brand)
laptop = Laptop(laptop_brand)

phone.show_info()
tablet.show_info()
laptop.show_info()

#Question 2
class Bank:
    def __init__(self, balance, new_amount):
        self.balance = balance
        self.new_amount = new_amount

    def add(self):
        self.balance += self.new_amount
        print(f"Current Balance: {self.balance}")

    def remove(self):
        self.balance -= self.new_amount
        print(f"Current Balance: {self.balance}")

account1 = Bank(150000, 500)

account1.add()
account1.remove()

#Question 3
from abc import ABC, abstractmethod

class Business(ABC):
    @abstractmethod
    def start_workday(self):
        print("Starting the work day")

    @abstractmethod
    def end_workday(self):
        print("Ending the workday")

class Little_Caesars(Business):
    def start_workday(self):
        print("Starting the work day for Little Caesars")

    def end_workday(self):
        print("Ending the workday for Little Caesars")

class Lowes(Business):
    def start_workday(self):
        print("Starting the work day for Lowes")

    def end_workday(self):
        print("Ending the workday for Lowes")

little_Caesars = Little_Caesars()
lowes = Lowes()

little_Caesars.start_workday()
lowes.start_workday()
little_Caesars.end_workday()
lowes.end_workday()

