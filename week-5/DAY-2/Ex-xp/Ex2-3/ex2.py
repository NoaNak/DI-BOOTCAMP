class Dog:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        print (f"{self.name} is barking")

    def run_speed(self):
        return self.weight / self.age*10

    def fight(self, other_dog):

        if self.run_speed()*self.weight > other_dog.run_speed()*other_dog.weight:
            print(f"{self.name}")
        else:
            print(f"{other_dog.name}")


dog1 = Dog('elie', 20, 15)
dog2 = Dog('gilles', 15, 10)
dog3 = Dog('lili', 10, 20)

dog1.bark()
dog1.run_speed()
dog1.fight(dog2)

dog2.bark()
dog2.run_speed()
dog2.fight(dog3)

dog3.bark()
dog3.run_speed()
dog3.fight(dog1)
