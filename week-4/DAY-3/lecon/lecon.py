# 1. keys and values

a_dict: dict = {}

print(type(a_dict))

# The key has to be NOT MUTABLE -> str, int
# b_dict = {[1,2,3]: "value"}

# print(b_dict)


c_dict = {1: "A", 2: "B"}

print(c_dict[1])

d_dict = {1: [1,2,3], 2: "Hello"}

info = {
    "Yossi": {"first_name": "yossi", "last_name": "eik", "age": 31},
    "David": {"first_name": "david", "last_name": "roz", "age": 28}
}

print(info["David"]["age"])

personal_info1 = {"name": "yossi", "City": "TLV"}
personal_info2 = {"name": "shon", "City": "AFULA"}
personal_info3 = {"name": "david", "City": "JERUSALEM"}
personal_info4 = {"name": "elie", "City": "KS"}
personal_info5 = {"name": "michel", "City": "NETANYA"}
personal_info6 = {"name": "ben"}

# print(personal_info.keys())

# keys

print(personal_info1.keys())
search_for = "City"
print(search_for in personal_info6.keys())
city_value = personal_info5.get("City", None)

print(city_value)


# values

dict_values = personal_info3.values()
print(dict_values)


# looping through keys
for key in personal_info1:
    print("KEY:", key)

# looping throug values
for value in personal_info1.values():
    print("VALUE:", value)

# looping through keys + values
for key, value in personal_info1.items():
    print(f"{key}: {value}")


# UPDATING
personal_info6 = {"name": "Noa"}
 
# Add a new key and value
personal_info6["City"] = "New York"

print(personal_info6)

personal_info6["NAME"] = personal_info6["name"]

del personal_info6["name"]

print(personal_info6)

personal_info6["NAME"] = "Lea"

print(personal_info6)



# 2. alphabet

alphabet ='abcdefghijklmnopqrstuvwxyz'
enumerated_alpha: dict = dict(enumerate(alphabet))

print(enumerated_alpha[2])

tasks = ['cleanup the apartments', 'cooking', 'go outside', 'jogging']
to_do = dict(enumerate(tasks, 1))

print(to_do)

# loop through index and value inside list 
for i, value in enumerate(tasks):
    print(f"INDEX {i} : {value}")


# 3. 
ages = [31, 28, 15, 12, 1]
names = ['Noa','Ethan', 'chely', 'Lina', 'Ruth']
cities = ['TLV', 'PARIS', 'NATANYA', 'TOULOUSE', 'MARSEILLE']


# 4.

even_numbers = []
range_numbers = 100

for num in range(range_numbers):
    if num % 2 == 0:
        even_numbers.append (num)
        # append pour rajouter un truc a la fin d'une liste

print(even_numbers)

# what to add for variable in sequence if condition

