# nstructions
# Écrivez un programme qui accepte une séquence de mots séparés par des virgules en entrée et imprime les mots dans une séquence séparée par des virgules après les avoir triés par ordre alphabétique.
# Utiliser la compréhension de liste

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

shlomo = Cat(cat_name='Shlomo', cat_age=4)
mizzy = Cat(cat_name='Mizzy', cat_age=3)
batya = Cat(cat_name='Batya', cat_age=5)

def oldest_cat(*cats):
    oldest_cat = cats[0]
    for cat in cats:
        if cat.age > oldest_cat.age:
            oldest_cat = cat

    print(f"Oldest cat: {oldest_cat.name}")

oldest_cat(batya, shlomo, mizzy)