#Dillon Bales 
#6/18/2025

#Question 1
class Pizza: 
    def __init__(self, dough, sauce, topping, cheese):
        self.dough = dough
        self.sauce = sauce
        self.topping = topping
        self.cheese = cheese

    def display_info(self):
        print(f"Crust: {self.dough}\nSauce: {self.sauce}\nTopping: {self.topping}\nCheese: {self.cheese}\n")
        
pizza1 = Pizza("thin crust", "tomato basil", "pepperoni", "mozzarella")
pizza2 = Pizza("deep dish", "bbq", "chicken", "cheddar")
pizza3 = Pizza("stuffed crust", "alfredo", "spinach", "parmesan")

class DessertPizza(Pizza):
    def __init__(self, dough, sauce, topping, cheese, fruit):
        super().__init__(dough, sauce, topping, cheese)
        self.fruit = fruit

    def display_info(self):
        print(f"Crust: {self.dough}\nSauce: {self.sauce}\nTopping: {self.topping}\nCheese: {self.cheese}\nFruit: {self.fruit}\n")

pizza4 = DessertPizza("whole wheat", "tomato", "ham", "mozzarella", "pineapple")
pizza5 = DessertPizza("gluten-free", "pesto", "prosciutto", "goat cheese", "figs")

pizza1.display_info()
pizza2.display_info()
pizza3.display_info()
pizza4.display_info()
pizza5.display_info()

#Question 2
class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0

    def __mul__(self, scalar):
        result = []
        for row in self.data:
            result.append([element * scalar for element in row])
        return Matrix(result)

    def __str__(self):
        return " ".join([f"({', '.join(map(str, row))})" for row in self.data])

    

matrix1 = Matrix([[1, 2], [3, 4]])

matrix2 = matrix1 * 3

print("Original Matrix:")
print(matrix1)

print("\nMatrix after multiplying by 3:")
print(matrix2)


#Question 3
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

account1 = Bank(1500, 100)

account1.add()
account1.remove()

#Question 4
from abc import ABC, abstractmethod

class Buisness(ABC):
    @abstractmethod
    def start_workday(self):
        print("Starting the work day")

    @abstractmethod
    def end_workday(self):
        print("Ending the workday")

class Walmart(Buisness):
    def start_workday(self):
        print("Starting the work day for Walmart")

    def end_workday(self):
        print("Ending the workday for Walmart")

class Maverik(Buisness):
    def start_workday(self):
        print("Starting the work day for Maverik")

    def end_workday(self):
        print("Ending the workday for Maverik")

walmart = Walmart()
maverik = Maverik()

walmart.start_workday()
maverik.start_workday()
walmart.end_workday()
maverik.end_workday()
        
        




    
