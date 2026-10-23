from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def identity(self):
        pass

class human(animal):
    def identity(self):
        print("I AM HUMAN")


class snake(animal):
    def identity(self):
        print("I AM SNAKE")


class lion(animal):
    def identity(self):
        print("I AM LION")


class monkey(animal):
    def identity(self):
        print("I AM MONKEY")


class dog(animal):
    def identity(self):
        print("I AM DOG")

h=human()
h.identity()

s=snake()
s.identity()

l=lion()
l.identity()

m=monkey()
m.identity()

d=dog()
d.identity()