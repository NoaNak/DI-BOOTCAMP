from translate import Translator

translate = Translator(from_lang="french", to_lang="english")

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 

dict1 = {}

for word in french_words:
    dict1[translate.translate(word)] = word

print(dict1)