class Farm:

    def __init__(self, farm_name):
        self.name = farm_name
        self.dic = {}

    def add_animal(self, name, ammount):
        if name not in self.dic:
            self.dic[name] = ammount
        else:
            self.dic[name] += ammount

    def get_animals_type(self):
        return(list(self.dic))

    def get_short_info(self):
        animals_joigned: ', '.join(self.get_animals_type())
        print(f"{self.name} has {self.get_animals_type()}")

Noa = Farm("noa")
Noa.add_animal("lili", 2)
Noa.get_short_info()
Noa.animals_joigned


