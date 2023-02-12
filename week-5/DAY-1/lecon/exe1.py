class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Hello my name is " + self.name)

    def change_name(self, name): 
        self.name = name

# Create a method that modifies the name of the person

first_person = Person("John", 36)

print(first_person.name)

first_person.change_name('Joe')

print(first_person.name)
