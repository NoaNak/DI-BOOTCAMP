class Israel:

    population = 0 # class variable

    @classmethod
    def print_population(cls):
        print(f"Israel now has a population of: {cls.population}")

class IsraeliCitizen(Israel):

    def __init__(self, name: str):
        self.name = name # object variable/attribute
        Israel.population += 1 


citizen1 = IsraeliCitizen('Shlono')
citizen2 = IsraeliCitizen('Eli')
citizen3 = IsraeliCitizen('Noa')


Israel.print_population()

