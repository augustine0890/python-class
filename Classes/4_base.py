from abc import ABC, abstractmethod

class Base(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass


class Real(Base):
    def foo(self):
        print('foo in Real')
    
    def bar(self):
        print('bar in Real')
    
    def other(self):
        pass


class Fake(Base):
    def foo(self):
        print('foo in Fake')


r = Real('Jane')
print(r.name)

# ABC - cannot instantiate the base-class
# b = Base('Boss')

# ABC - must implement methods
# f = Fake('Joe')