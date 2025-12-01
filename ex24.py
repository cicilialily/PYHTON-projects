


# animal is-object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass
# ??
class Dog(Animal):
    def __int__(self, name):
        self.name = name

# ??
class Cat(Animal):
    def __init__(self, name):
        self.name = name

class Person(object):
    def __init__(self, name):
        self.name = name

        self.pet = None

class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)

class Fish(object):
    pass

class Salmon:
    pass

class Halibut(Fish):
    pass


satan = Cat("satan")

mary = Person("mary")
mary.pet = satan

frank = Employee("frank", 120000)

frank.pet = Cat

flipper = Fish()

course = Salmon()
harry = Halibut()

