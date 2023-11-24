# Hirachical inheritance
class Animal:
    def __init__(self, species):
        self.species = species

    def sound(self):
        pass


class Dog(Animal):
    def __init__(self, breed):
        super().__init__('Canine')
        self.breed = breed

    def sound(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, breed):
        super().__init__('Feline')
        self.breed = breed

    def sound(self):
        return "Meow!"

class Cow(Animal):
    def __init__(self, breed):
        super().__init__('Bovine')
        self.breed = breed

    def sound(self):
        return "Moo!"


dog = Dog('Labrador')
cat = Cat('Siamese')
cow = Cow('Holstein')

print(f"The {dog.species} {dog.breed} says: {dog.sound()}")
print(f"The {cat.species} {cat.breed} says: {cat.sound()}")
print(f"The {cow.species} {cow.breed} says: {cow.sound()}")

#----------------------------------------------------------------------------------------

# Hybrid inheritance
# Parent class 1
class Animal:
    def __init__(self, species):
        self.species = species

    def sound(self):
        pass

# Parent class 2
class Pet:
    def __init__(self, name):
        self.name = name

    def play(self):
        pass

# Child class inheriting from Animal and Pet
class Dog(Animal, Pet):
    def __init__(self, breed, name):
        Animal.__init__(self, 'Canine')
        Pet.__init__(self, name)
        self.breed = breed

    def sound(self):
        return "Woof!"

    def play(self):
        return f"{self.name} the {self.breed} is playing fetch."

# Another child class inheriting from Animal
class WildAnimal(Animal):
    def hunt(self):
        return "This wild animal is hunting."

# Grandchild class inheriting from WildAnimal
class Tiger(WildAnimal):
    def __init__(self, species):
        super().__init__(species)

    def sound(self):
        return "Roar!"

# Creating instances of the classes
dog = Dog('Labrador', 'Buddy')
tiger = Tiger('Wild Cat')

# Accessing attributes and methods
print(f"The {dog.species} {dog.breed} named {dog.name} says: {dog.sound()}")
print(dog.play())

print(f"The {tiger.species} says: {tiger.sound()}")
print(tiger.hunt())
