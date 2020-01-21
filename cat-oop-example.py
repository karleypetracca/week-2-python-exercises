# Classroom example: Object oriented programming: Cat class exercises

class Cat:
    # class attributes
    species = "mammal"
    legs = 4
    eyes = 2
    tail = 1
    fur = True

    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return "{} is {} years old: {}".format(self.name, self.age, Cat.legs)

    def update_age(self, new_age):
        self.age = new_age

gus = Cat("Gus", 10)

# Call description and class attributes not in init
print(gus.description())
print(gus.species, gus.legs, gus.eyes)

# Change Class instance attribute
print(gus.update_age(11))
print(gus.age, gus.description())