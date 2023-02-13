class Pets():

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():

    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Siamese(Cat):
    pass

class Bengal(Cat):

    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):

    def sing(self, sounds):
        return f'{sounds}'


all_cats = [Bengal("bob", 23), Chartreux("carl", 10), Siamese("gilles", 45)]
sara_pets = Pets(all_cats)

sara_pets.walk()

# si je veux faire une loop je peux faire 
# for cat in all_cats:
#     print (cat.walk())
