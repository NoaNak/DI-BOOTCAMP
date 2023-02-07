#CHALLENGE 1

# 1. Ask the user for a number and a length.
user_number: int = int(input("Your number: "))
user_length: int = int(input("Your length: "))

result = []

# 2. Create a program that prints a list of multiples of the number until the list length reaches length.
for multipler in range(user_length):
    result.append(user_number * multipler)

print(result)

#CHALLENGE 2 

# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
