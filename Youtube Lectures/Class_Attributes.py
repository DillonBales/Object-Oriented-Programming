
class Person:
    number_of_people = 0 #This will be true for all objects beause it does not use "self"

    def __init__(self, name):
       self.name = name 
       Person.add_person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1  

p1 = Person("Tim")
# print(Person.number_of_people)
p2 = Person("Jill")
print(Person.number_of_people_())

# Person.number_of_people = 8
# print(p2.number_of_people)
# print(p1.number_of_people)
