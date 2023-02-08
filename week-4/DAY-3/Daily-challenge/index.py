# dict = {}
user = input("Write a word: ")

result = {}

for i, letter in enumerate(user):
    # (i) est le numero
    if letter in result:
       result[letter].append(i)

    else: 
         result[letter] = [i]

print(result)
