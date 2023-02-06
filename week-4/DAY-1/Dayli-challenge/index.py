num_character: str = input("Give me a string:")
if len(num_character) < 10:
    print("string not long enough")
elif len(num_character) > 10 :
    # len c pour me renvoyer a une fonction
    print("string too long")
else:
    print("Correct")

    first_char: str = num_character[0]
    last_char: str = num_character[-1]

    print(f"first character: {first_char} | last character: {last_char}")

result: str = ""
for char in num_character:
    result += char
    print(result)

# bonus
# not mutable - cannot be changed

# 1. Change the type of the string into a list 
# LIST - mutable, sequential collection of items
 
# num_charactere = list(num_charactere)
# print(num_charactere)

# 2. Use the list to shuffle all of characters 
# random.shuffle(num_character)
# print(num_character)

# 3. to bring the shuffle type back into a string
num_character: str = "".join(num_character)
print(num_character)


# text.upper = mettre tout en majuscule
# text.capitalize = mettre la premiere lettre en majuscule
# si je veux acceder a une fonction string alors je dois mettre un . avant la fonction