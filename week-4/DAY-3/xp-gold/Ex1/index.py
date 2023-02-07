# 1. Create a variable called birthdays. Its value should be a dictionary.
# 2. Initialize this variable with birthdays of 5 people of your choice. For each entry in the dictionary, the key should be the person’s name, and the value should be their birthday. Tip : Use the format “YYYY/MM/DD”.

birthdays = {
    "Noa": "24/08/2002",
    "Ethan": "03/03/2001",
    "Chely": "14/08/2000",
    "Taly": "17/03/2007",
}


# 3. Print a welcome message for the user. Then tell them: “You can look up the birthdays of the people in the list!”

print("You can look up the birthdays of the people in the list!")


# 4. Ask the user to give you a person’s name and store the answer in a variable.

name = input("Person name: ")


# 5. Get the birthday of the name provided by the user.

birthday = birthdays.get(name, f"THERE is no {name} in the data")


# 6. Print out the birthday with a nicely-formatted message.

print(birthday)