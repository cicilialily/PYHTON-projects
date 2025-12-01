# Animal is the base class
class Animal(object):
    pass

# Dog is a subclass of Animal
class Dog(Animal):
    def __init__(self, name):  # Fixed the constructor
        self.name = name

# Cat is a subclass of Animal
class Cat(Animal):
    def __init__(self, name):
        self.name = name

# Person class
class Person(object):
    def __init__(self, name):
        self.name = name
        self.pet = None  # Initially, a person has no pet

# Employee is a subclass of Person
class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)  # Call the parent constructor
        self.salary = salary  # Add salary attribute

# Fish is the base class for aquatic animals
class Fish(object):
    pass

# Salmon is a subclass of Fish
class Salmon(Fish):
    pass

# Halibut is a subclass of Fish
class Halibut(Fish):
    pass

# Create instances of the classes
satan = Cat("Satan")  # Cat instance

mary = Person("Mary")  # Person instance
mary.pet = satan  # Assign Satan as Mary's pet

frank = Employee("Frank", 120000)  # Employee instance
frank.pet = Cat("Whiskers")  # Assign a new Cat instance as Frank's pet

flipper = Fish()  # Fish instance
course = Salmon()  # Salmon instance
harry = Halibut()  # Halibut instance

# Display some of the relationships
print(f"{mary.name} has a pet named {mary.pet.name}.")
print(f"{frank.name} has a pet named {frank.pet.name} and earns {frank.salary}.")

