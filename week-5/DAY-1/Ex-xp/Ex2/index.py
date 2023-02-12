# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.


class Dog():

    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height} cm high!")


davids_dog = Dog("Rex", 50)
sarahs_dog = Dog ("Teacup", 20)

print()
davids_dog.bark()
davids_dog.jump()

print(f"Sarah's dog's name is {sarahs_dog.name} and height is {sarahs_dog.height} cm.")

sarahs_dog.bark()
sarahs_dog.jump()


def winner():
    if davids_dog.height > sarahs_dog.height:
        print(f"{davids_dog.name} is bigger.")
    else:
        print(f"{sarahs_dog.name} is bigger.")

winner()


f"David's dog's name is {davids_dog.name} and height is {davids_dog.height} cm."