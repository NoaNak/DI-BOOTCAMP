dict = {}
word = input("write a word: ")
for i, letter in enumerate(word):
    if letter not in  dict:
        dict[letter] = []
        dict[letter].append(i)

print(dict)
