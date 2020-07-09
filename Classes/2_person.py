class Person:
    count = 0
    def __init__(self, name):
        self.name = name
        self.count += 1

    def show(self):
        return self.name



jane = Person("Jane")
print(jane.show())

def new_show(some_instance):
    print("Hello " + some_instance.name)

Person.show = new_show
jane.show()