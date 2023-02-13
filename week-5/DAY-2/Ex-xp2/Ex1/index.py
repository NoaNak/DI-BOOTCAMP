class Family:
    
    def __init__(self, lastname, members:list):
        self.members = members
        self.lastname = lastname
        
    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations to the family")

    def is_18(self, name):
        for member in self.members:
            if name == member["name"] and member["age"] > 17:
                return True
        return False

    def family_presentation(self):
        for member in self.members:
            print(member["name"])
        print(self.lastname)
        

fam = Family("Nakache", [
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
]) 

fam.born(name = "Noa", age = 20, gender = "female", is_child = False)

     
