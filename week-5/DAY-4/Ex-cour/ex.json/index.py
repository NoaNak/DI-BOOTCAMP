import json

# Open the JSON file and load the data into a variable called "family"
file_location = "file.json"

jane_info = {}

with open(file_location, "r") as file: # r = read le dossier
    jane_info = json.load(file)

# Print nicely details about Jane's children
for child in jane_info["children"]:
    print(child["firstName"])
    print(child["age"])

# Inside the family variable, add to each children, a key 'favorite_color' with a value
for child in jane_info["children"]:
    child["favorite_color"] = "blue"

print(jane_info["children"])

# Then, save back all the new data into the json file
with open(file_location, "w") as file: # w c est pour write le file
    json.dump(jane_info, file, indent = 4) # pour enregistrer le dict dans le json file 
