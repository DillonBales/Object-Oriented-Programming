#Dillon Bales 
#5/16/2025

class Car:
    #Give Car "traits"
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    #Display given infomation
    def display_info(self):
        print(f"This car is a {self.year} {self.brand} {self.model} with {self.mileage} miles on it.")

class ElectricCar(Car):
    #Give ElectricCar "traits" without overriding the ones from Car
    def __init__(self, brand, model, year, mileage, battery_capacity):
        super().__init__(brand, model, year, mileage)
        self.battery_capacity = battery_capacity

    #Display given infomation
    def display_info(self):
        print(f"This car is a {self.year} {self.brand} {self.model} with {self.mileage} miles on it. It also has a battery capacity of {self.battery_capacity} kWh")

#Initiating Objects
car1 = Car("Toyota", "Camry", 2018, 52300)
car2 = Car("Ford", "Mustang", 2021, 18750)
car3 = Car("Honda", "Civic", 2016, 89420)

electricCar1 = ElectricCar("Tesla", "Model 3", 2022, 15230, 75)
electricCar2 = ElectricCar("Nissan", "Leaf", 2020, 28700, 40)

#Testing Methods
car1.display_info()
car2.display_info()
car3.display_info()

electricCar1.display_info()
electricCar2.display_info()