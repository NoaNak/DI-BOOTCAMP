from random import choice

file_location = r"C:\Users\noana\Desktop\sublime-text\DI-exercises-projects\week-5\DAY-4\Ex-xp1\list.txt"

def get_words_from_file(file_name):
    with open(file_name) as f: #pour ouvir le file 
        words = f.readlines()
        words = [word.replace("\n", "") for word in words ] #pour que tout les mots sois chacun a la ligne 
        return words

get_words_from_file(file_location) #apl la fonction et lui dire quel dossier je veux pour utiliser cette fct

def get_random_sentence(file, length):
    sentence = []
    for word in range(length):
        sentence.append(choice(get_words_from_file(file)))
    print(sentence)

# get_random_sentence(file_location, 4)

def main():
    print("The program takes your chosen length between 2-20 and generates a random sentence ")
    number = int(input("Please enter a length: "))
    if 2 <= number | number <= 20:
        get_random_sentence(file_location, number)
    else:
        raise ValueError

main()