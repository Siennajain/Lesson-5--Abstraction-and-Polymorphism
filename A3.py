from abc import ABC,abstractmethod
class absclass(ABC):

    def print(self,x):
        print("Value:",x)

    @abstractmethod
    def inside(self):
        print("WE ARE INSIDE ABSCLASS")

class test(absclass):
    def inside(self):
        print("WE ARE INSIDE TEST")

t=test()
t.inside()
t.print(300)