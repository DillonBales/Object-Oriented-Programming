#Object Oriented Programming in Python

#Objects are the things used within a class

# def hello():
#     print("hello")

# x = 1
# print(type(hello))

# x = 1
# y = "hello"

# print(x+y)

# string = "hello"
# print(string.upper()) #any time there is a . after a object it is a method that is acting on an object

class Dog:

    def __init__(self, name, age):  #Attribute of the class dog, which is name. This lets the class save the name
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age

    # def add_one(self, x):
    #     return x + 1

    # def bark(self):
    #     print("bark")

d = Dog("Tim", 3)
d.set_age(23)
print(d.get_age())
# d2 = Dog("Bill", 12)
# print(d2.get_age())
# d.bark()
# print(d.add_one(5))

# print(type(d))
