import json

my_family = {
    "parents": ['Beth', 'Jerry'],
    "children": ['Summer', 'Morty']
}

file_location = 'family2.json'

with open(file_location, 'w') as file:
    json.dump(my_family, file) # dump - saves a python dictionary (my_family) into a file (file)


