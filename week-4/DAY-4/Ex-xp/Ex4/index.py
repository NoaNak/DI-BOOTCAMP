# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.

import random

def number (user_number):
    computer_number = random.randint(1, 100)
    #ran = random + int 
    if computer_number == user_number:
        print("bravooo vous avez reussi !")
    else:
        print("Vous avez echouer ...")
        print(f"The computer number is {computer_number} and the user number is {user_number}")


number(24)
#si je veux pas mettre de parametre jecris pass