# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# total_cost = 0

# for name, age in family.items():
#     if age < 3:
#         print(f"{name}the ticket is free !")

#     elif age >= 3 and age <= 12:
#         print(f"{name}the ticket is $10")
#         total_cost += 10


#     else:
#         print(f"{name}the ticket is $15.")
#         total_cost += 15
# age = 0 

# How much does each family member have to pay ?
# Print out the family’s total cost for the movies.
# Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).
# print(total_cost)
 
total_cost = 0

family = {}
name = input("Enter your name: ")
age = int(input("Enter your age: "))

family[name] = age
print(family)

for name, age in family.items():
    if age < 3:
        print(f"{name}the ticket is free !")

    elif age >= 3 and age <= 12:
        print(f"{name}the ticket is $10")
        total_cost += 10

    else:
        print(f"{name}the ticket is $15.")
        total_cost += 15
age = 0 


