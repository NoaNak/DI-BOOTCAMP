import json 

my_family = {}

file_location = 'family2.json'

with open(file_location, 'r') as file:
    my_family = json.load(file)

print(my_family)