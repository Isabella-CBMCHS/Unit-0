'''
############
# Lab 0.04 #
############

Overview
--------
Given the following Sample Code, practice using inheritance 
to create specific child classes for different types of Pokemon.

Create the three child classes below:
1. Water Type
When attacking a fire type, the attack is more effective

When attacking a grass type the effect is less effective

When growl is called print out Splish Splash

2. Fire Type
When attacking a water type, the attack is less effective

When attacking a grass type the effect is more effective

When growl is called print out "Fire Fire"

3. Grass Type
When attacking a water type, the attack is more effective

When attacking a fire type the effect is less effective

When growl is called print out "Cheep Cheep"

##############################################################
# Note: In order to check what type an object is you can use #
# isinstance which takes in an object, a class and returns a #
# Boolean if the object is the type of the inputted class.   #
##############################################################

Example Code
------------
my_pet = Pet()
isinstance(my_pet, Pet) # returns true
isinstance(my_pet, Dog) # returns false
'''
# Pokemon Project (Isabella)

class User:
    def __init__(self, name):
        self.name = name
        self.pokemon = []
        self.current_pokemon = None

    def switch(self):
        pass

    def heal(self):
        pass

    def attack(self, target, attack_name):
        pass

    def print_choices(self, poke_list):
        print(f"{self.name}, welcome to the wonderful world of Pokemon! Please consider the following list: ")
        num = 1
        for poke in poke_list:
            print(f"{num}. {poke.name} - HP: {poke.health} ~ AP: {poke.attack_points}")
            num += 1

    # populates player's hand of pokemon
    def poke_choices(self, poke_list):
        for i in range(3):
            self.print_choices(poke_list)
            poke_choice = int(input(f"Go on! Select a Pokemon, {self.name}:")) - 1
            self.pokemon.append(poke_list[poke_choice])
            poke_list.remove(poke_list[poke_choice])
            
                
    def get_attack_power(self):
        pass

    def is_end_game(self):
        pass

    def print_attacks(self):
        pass


class Computer(User):
    def play_turn(self):
        pass

    def set_pokemon(self):
        import random
        pokemon_list = [poke1, poke2, poke3, poke4, poke5, poke6, poke7, poke8, poke9]
        r = random.choice(pokemon_list)
        print(r)

    def attack(self):
        pass

    def switch(self):
        pass


class Pokemon():
    def __init__(self, name, hp, ap):
        self.name = name
        self.health = hp
        self.attack_points = ap
        self.type = self.set_type()  
        self.cry = self.set_cry()
        self.attacks = self.set_attacks()

    def growl(self):
        print(self.cry)

    def attack(self, other):
        self.attack_results(other)


class FireType(Pokemon):
    def set_type(self):
        return "fire"

    def set_cry(self):
        return "Fire Fire"

    def set_attacks(self):
        # set dictionary with "attack name": [power, accuracy]
        return {
                "Ember": [60, 100],
                "Fire Punch": [85, 80],
                "Flame Wheel": [70, 90]
                 }

    def attack_results(self, other):
        self.growl()
        # vs water
        if isinstance(other, WaterType):
            print(f"{self.name}'s attack is LESS effective against {other.type}.")

        # vs grass
        if isinstance(other, GrassType):
            print(f"{self.name}'s attack is MORE effective against {other.type}.")

    def get_attack_power(self):
        pass


class WaterType(Pokemon):
    def set_type(self):
        return "water"

    def set_cry(self):
        return "Splish Splash"

    def attack_results(self, other):
        self.growl()
        # vs water
        if isinstance(other, GrassType):
            print(f"{self.name}'s attack is LESS effective against {other.type}.")

        # vs grass
        if isinstance(other, FireType):
            print(f"{self.name}'s attack is MORE effective against {other.type}.")

    def set_attacks(self):
        # set dictionary with "attack name": [power, accuracy]
        return {
                "Bubble": [40, 100],
                "Hydro Pump": [185, 30],
                "Surf": [70, 90]
                 }

        def get_attack_power(self):
            pass


class GrassType(Pokemon):
    def set_type(self):
        return "grass"

    def set_cry(self):
        return "Cheep Cheep"

    def attack_results(self, other):
        self.growl()
        # vs water
        if isinstance(other,FireType):
            print(f"{self.name}'s attack is LESS effective against {other.type}.")

        # vs grass
        if isinstance(other, WaterType):
            print(f"{self.name}'s attack is MORE effective against {other.type}.")

    def set_attacks(self):
        # set dictionary with "attack name": [power, accuracy]
        return {
                "Leaf Storm": [130, 90],
                "Giga Drain": [50, 100],
                "Razor Leaf": [55, 95]
                 }
    
    def get_attack_power(self):
        pass


# pokemon instances
poke1 = FireType("Charmander", 25, 70)
poke2 = FireType("Ninetails", 30, 50)
poke3 = FireType("Ponyta", 40, 60)
poke4 = WaterType("Squirtle", 80, 20)
poke5 = WaterType("Psyduck", 70, 40)
poke6 = WaterType("Polywag", 50, 50)
poke7 = GrassType("Bulbasaur", 60, 40)
poke8 = GrassType("Bellsprout", 40, 60)
poke9 = GrassType("Oddish", 50, 50)

pokemon_list = [poke1, poke2, poke3, poke4, poke5, poke6, poke7, poke8, poke9]

### SET UP USERS ##
# user names
player_name = input("Welcome player, what is your name?")
computer_name = input("What is the name of your rival?")
# instantiate user objects
player = User(player_name)
computer = Computer(computer_name)
# player chooses three pokemon
player.poke_choices(pokemon_list)

print(player.pokemon)
player.print_choices(pokemon_list)


