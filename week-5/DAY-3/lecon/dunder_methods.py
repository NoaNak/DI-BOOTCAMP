class Person: 

    def __init__(self, first_name: str, last_name: str, residence: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.residence = residence
        self.age = age

    # dunder - double underscores. dunder method is a method with __ underscores on each side
    def __str__(self) -> str: # str is for everyone 
        fullname = f'{self.first_name} {self.last_name}'
        return fullname

    def __repr__(self) -> str: # repr is for the developer (more technical)
        return f'{str(self)}, id: {id(self)}'

    def __add__(self, value) -> int:  # __add__ <-> + 
        return self.age + value

    def __iadd__(self, value) -> None: # __iadd__ <-> += 
        self.age += value
        return self

    def full_info(self) -> str:
        full_info = f'{str(self)}\nage: {self.age}\nresidence: {self.residence}'
        return full_info



person1 = Person('Badu', 'Complication', 'Nigeria', 17)
person2 = Person('Maria', 'Chris', 'Russia', 43)
print(person1)
print(person1.full_info())

print(person2 + 1)
print(person2.age)

person2 += 1
print(person2.full_info())

print(repr(person1))
print(person1.__repr__())