from datetime import datetime

class Person:
    def __init__(self, years):
        self.age = years
    
    # creates "getter"
    @property
    def age(self):
        return datetime.now().year - self.birthyear
    
    # creates "setter"
    @age.setter
    def age(self, years):
        if years < 0:
            raise ValueError("Age cannot be negative")
        self.birthyear = datetime.now().year - years

p = Person(29)
print(p.age)

p.age = p.age + 1
print(p.age)

p.birthyear = 1990
print(p.age)

p2 = Person(-10)