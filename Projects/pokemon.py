class Pokemon:
    def __init__(self, name, type, level = 5):
        self.name = name
        self.level = level
        self.type = type
        self.max_health = level
        self.health = self.max_health
        self.is_knocked_out = False

    def lose_health(self, lose):
        self.health -= lose
        if self.health <= 0:
            self.health = 0
            self.knock_out()
        print("{name} now has {health}".format(name=self.name, health=self.health))
    
    def gain_health(self, gain):
        self.health += gain
        print("{name} gained {gain} health.".format(name=self.name, gain=gain))
        print("{name} now has {health}".format(name=self.name, health=self.health))
    
    def knock_out(self):
        if self.is_knocked_out:
            print("{name} is already knocked out.".format(name=self.name))
        else:
            self.is_knocked_out = True
            print("{name} is knocked out!".format(name=self.name))

    def revive(self):
        self.is_knocked_out = False
        if self.health == 0:
            self.health = 1
        print("{name} was revived!".format(name = self.name))

    def attack(self, other_pokemon):
        if self.is_knocked_out:
            print("You can't attack. {pokemon} is knocked out!".format(pokemon=self.name))
            return
        
        if (self.type == "Water" and other_pokemon.type == "Grass") or (self.type == "Fire" and other_pokemon.type == "Water") or (self.type == "Grass" and other_pokemon.type == "Fire"):
            print("{pokemon} attacked {other_pokemon} for {damage} damage.".format(pokemon=self.name, other_pokemon=other_pokemon.name, damage= round(self.level * 0.5)))
            other_pokemon.lose_health(round(self.level * 0.5))
        
        if (self.type == other_pokemon.type):
            print("{pokemon} attacked {other_pokemon} for {damage} damage.".format(pokemon = self.name, other_pokemon = other_pokemon.name, damage = self.level))
            other_pokemon.lose_health(self.level)

        if (self.type == "Fire" and other_pokemon.type == "Grass") or (self.type == "Water" and other_pokemon.type == "Fire") or (self.type == "Grass" and other_pokemon.type == "Water"):
            print("{pokemon} attacked {other_pokemon} for {damage} damage.".format(pokemon = self.name, other_pokemon = other_pokemon.name, damage = self.level * 2))
            other_pokemon.lose_health(self.level * 2)

    def __repr__(self):
        return "Pokemon info: {}, current level: {}, type: {}, maximun health: {}, current health: {}.\n".format(self.name, self.level, self.type, self.max_health, self.health)


class Trainer:
    def __init__(self, pokemons, potions, name):
        self.pokemons = pokemons
        self.potions = potions
        self.current_pokemon = 0
        self.name = name

    def attack_other_trainer(self, other_trainer):
        my_pokemon = self.pokemons[self.current_pokemon]
        their_pokemon = other_trainer.pokemons[other_trainer.current_pokemon]
        my_pokemon.attack(their_pokemon)

    def __repr__(self):
        print("The trainer {name} has the following pokemon".format(name = self.name))
        for pokemon in self.pokemons:
            print(pokemon)
        return "The current active pokemon is {name}".format(name = self.pokemons[self.current_pokemon].name)

class Charmander(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Charmander", "Fire", level)

class Squirtle(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Squirtle", "Water", level)

class Bulbasaur(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Bulbasaur", "Grass", level)


squirtle = Pokemon("Squirtle", "Water", 2)
pikachu = Pokemon("Pikachu", "Fire", 5)
bulbasaur = Pokemon("Bulbasaur", "Grass", 5)

print(bulbasaur)
print(pikachu)

pikachu.lose_health(1)
pikachu.gain_health(1)

a = Charmander(7)
b = Squirtle()
c = Squirtle(1)
d = Bulbasaur(10)
e = Charmander()
f = Squirtle(2)

trainer_one = Trainer([a,b,c], 3, "Alex")
trainer_two = Trainer([d,e,f], 5, "Sara")

print(trainer_one)
print(trainer_two)

trainer_one.attack_other_trainer(trainer_two)
trainer_two.attack_other_trainer(trainer_one)





