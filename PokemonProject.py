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
        print(f"{party}: {poke1.name} - {poke1.ap}, {poke1.hp}. {poke2.name} - {poke2.ap}, {poke2.hp}. {poke3.name} - {poke3.ap}, {poke3.hp}.")
        int(input(f">>> Please select a Pokemon to switch to:"))

    def heal(self):
        x = Pokemon.hp
        y = 20

        sum = x + y

        print(f">>>{current_pokemon}'s HP is now {sum}.")

    def attack(self, target, attack_name):
        pass
        # ??? input mayb? self = current pkmon, what abt target? input would b attack name (names in dictionary already)

    def attack_power(self):
        # random num b/t pkmon ap and pkmon ap - 20 UNLESS move pp (power points) is lower than ap 
        # charmander has 70 ap but ember is max 60 pp, so attack power is a random num b/t 60-40 instead of 70-50!!
        pass

    def print_choices(self, poke_list):
        print(f">>> {self.name}, welcome to the wonderful world of Pokemon! Please consider the following list: ")
        num = 1
        for poke in poke_list:
            print(f"{num}. {poke.name} - HP: {poke.health} ~ AP: {poke.attack_points}")
            num += 1

    # populates player's hand of pokemon (party)
    def poke_choices(self, poke_list):
        for i in range(3):
            self.print_choices(poke_list)
            poke_choice = int(input(f">>> Go on! Select a Pokemon, {self.name}.")) - 1
            self.pokemon.append(poke_list[poke_choice])
            poke_list.remove(poke_list[poke_choice])

        '''v  three chosen pokemon'''
    def party(self):
        # list? of three pkmon chosen @ beginning - list = partpoke1, partpoke2, etc??? parpoke/partpoke/partypoke 
        pass

    def is_end_game(self):
        # checks to see if all pkmon have fainted for either comp or player
        pass

    def print_attacks(self):
        print(FireType.set_attacks, WaterType.set_attacks, GrassType.set_attacks)

    def stats(self):
        print(f"{current_pokemon}: {Pokemon.name} - {Pokemon.ap}, {Pokemon.hp}.")
    
    def current_pokemon(self):
        # pkmon player is currently using (one of three chosen @ beginning)
        pass


class Computer(User):
    def play_turn(self):
        # attack (2/3), heal (1/6), switch (1/6)
        pass

    # randomly selects computer's pokemon
    def set_pokemon(self, firetype_list, watertype_list, grasstype_list):
        import random
        print(f">>> Oh? It seems {rival_name} has chosen {random.choice(firetype_list).name}, {random.choice(watertype_list).name}, and {random.choice(grasstype_list).name}.")
 
    def attack(self):
        print(FireType.set_attacks, WaterType.set_attacks, GrassType.set_attacks)

    def switch(self):
        # current pkmon -> randomly select diff pkmon from party
        pass


class Pokemon():
    def __init__(self, name, hp, ap):
        self.name = name
        self.health = hp
        self.attack_points = ap
        self.type = self.set_type()  
        self.cry = self.set_cry()
        self.attacks = self.set_attacks()
        self.attack_power = self.get_attack_power

    def growl(self):
        print(self.cry)

    def attack(self, other):
        self.attack_results(other)
    
    def get_attack_power(self):
        import random
        # attack power
        num1 = random.randint(Pokemon.ap, Pokemon.ap - 20)

    def take_damage(self):
        # same method as heal, subtr?
        x = Pokemon.get_attack_power
        #just ^ this/w-o x#
        y = Pokemon.ap

        sum = x + y
        #add input & need random 

    def heal(self):
        # x = current pkmon?
        x = Pokemon.hp
        y = 20

        sum = x + y

        print(f"{current_pokemon}'s HP is now {sum}.")


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
            print(f"{self.name}'s attack is NOT VERY EFFECTIVE against {other.type}.")

        # vs grass
        if isinstance(other, GrassType):
            print(f"{self.name}'s attack is SUPER EFFECTIVE against {other.type}.")
 
    def get_attack_power(self):
        import random

        num1 = random.randrange(FireType.ap, FireType.ap - 20)
        print(f"{current_pokemon} did {num1} damage!")


class WaterType(Pokemon):
    def set_type(self):
        return "water"

    def set_cry(self):
        return "Splish Splash"

    def attack_results(self, other):
        self.growl()
        # vs water
        if isinstance(other, GrassType):
            print(f"{self.name}'s attack is NOT VERY EFFECTIVE against {other.type}.")

        # vs grass
        if isinstance(other, FireType):
            print(f"{self.name}'s attack is SUPER EFFECTIVE against {other.type}.")

    def set_attacks(self):
        # set dictionary with "attack name": [power, accuracy]
        return {
                "Bubble": [40, 100],
                "Hydro Pump": [185, 30],
                "Surf": [70, 90]
                 }

    def get_attack_power(self):
        import random

        num1 = random.randrange(WaterType.ap, WaterType.ap - 20)
        print(f"{current_pokemon} did {num1} damage!")


class GrassType(Pokemon):
    def set_type(self):
        return "grass"

    def set_cry(self):
        return "Cheep Cheep"

    def attack_results(self, other):
        self.growl()
        # vs water
        if isinstance(other,FireType):
            print(f"{self.name}'s attack is NOT VERY EFFECTIVE against {other.type}...")

        # vs grass
        if isinstance(other, WaterType):
            print(f"{self.name}'s attack is SUPER EFFECTIVE against {other.type}.")

    def set_attacks(self):
        # set dictionary with "attack name": [power, accuracy]
        return {
                "Leaf Storm": [130, 90],
                "Giga Drain": [50, 100],
                "Razor Leaf": [55, 95]
                 }
    
    def get_attack_power(self):
        import random

        num1 = random.randrange(GrassType.ap, GrassType.ap - 20)
        print(f"{current_pokemon} did {num1} damage!")


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
firetype_list = [poke1, poke2, poke3]
watertype_list = [poke4, poke5, poke6]
grasstype_list = [poke7, poke8, poke9]

### SET UP USERS ##
# user names
player_name = input(">>> Welcome player, what is your name?")
rival_name = input(">>> What is the name of your rival?")
# instantiate user objects
player = User(player_name)
rival = Computer(rival_name)
# player chooses three pokemon
player.poke_choices(pokemon_list)

print(player.pokemon)
player.print_choices(pokemon_list)
rival.set_pokemon(firetype_list, watertype_list, grasstype_list)

Pokemon.attack(poke1, poke4)
#testing ^


'''
# game over? (for you)
if game_over(player):
    print(f">>> All of {player}'s pokemon have fainted. {player} whited out!")

# game over? (for opponent/comptuer)
if game_over(rival):
    print(f">>> {rival_name} has been defeated. {player} won the battle!")
'''