from ex2 import Dog
import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name,age,weight)
        self.trained = False

    def train(self):
        self.bark()
        self.trained = True

    def play(self, *args):
        print(f"{self.name} all play together")

    def do_a_trick(self):
        if self.trained == True:
            x = random.randint(0,3)
            if x == 0:
                print(f"{self.name} does a barrel roll")

            elif x == 1:
                print(f"{self.name} stands on his back legs")
            
            elif x == 2:
                print(f"{self.name} shakes your hand")

            else:
                print(f"{self.name} plays dead")






