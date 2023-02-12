class Player:
    def __init__(self, name: str, player_class: str, strength: int, health: int):
        # name
        self.name = name
        # player_class
        self.player_class = player_class
        # strength
        self.strength = strength
        # health
        self.health = health

    def fight(self):
        print(f'{self.name} is fighting !')
    
    def add_health(self, health: int):
        self.health += health
        print(f'{self.name} increased health to {self.health}')

warrior1 = Player('joe', 'warrior', 100, 100)
warrior2 = Player('yossi', 'codeman', 10, 1000)

print(warrior1.strength)
print(warrior2.strength)

warrior2.fight()

print(warrior1.health)

warrior1.add_health(50)



