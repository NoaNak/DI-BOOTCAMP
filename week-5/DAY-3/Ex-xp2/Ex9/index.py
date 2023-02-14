from faker import Faker

fake = Faker()

name = fake.name()

email = fake.email()

address = fake.address()

phone_number = fake.phone_number()

print(name)

users = []
dict = {}

def __add__(amount):
    for i in range(amount):
        dict["name"] = name
        dict["email"] = email
        dict["address"] = address
        users.append(dict)
    print(users)

__add__(3)