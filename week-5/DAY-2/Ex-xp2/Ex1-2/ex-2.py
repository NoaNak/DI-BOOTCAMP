from index import Family
import random

class TheIncredibles(Family):  
    def __init__(self, lastname ,members):
        super().__init__(lastname, members)

    def use_power(self, name):
        for member in self.members:
            if name == member["name"] and member["age"] > 17:
                print(member["power"])
        else:
            print("You have no power")
            
    def incredible_presentation(self):
        for member in self.members:
            print(member["name"])

fam = TheIncredibles ("Nakache",[
    {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
])

fam.incredible_presentation()