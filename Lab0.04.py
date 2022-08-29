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
class Pokemon():
    def __init__(self, name):
        self.name = name
        self.type = self.set_type()  
        self.cry = self.set_cry()

    def growl(self):
        print(self.cry)

    def attack(self, other):
        self.attack_results(other)

class FireType(Pokemon):
    def set_type(self):
        return "fire"

    def set_cry(self):
        return "Fire Fire"

    def attack_results(self, other):
        self.growl()
        # vs water
        if isinstance(other, WaterType):
            print(f"{self.name}'s attack is LESS effective against {other.type}.")

        # vs grass
        if isinstance(other, GrassType):
            print(f"{self.name}'s attack is MORE effective against {other.type}.")


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


# pokemon instances
poke1 = FireType("Charmander")
poke2 = WaterType("Squirtle")
poke3 = GrassType("Bulbasaur")

# fire attacks
poke1.attack(poke2)
poke1.attack(poke3)

# water attacks
poke2.attack(poke1)
poke2.attack(poke3)

# grass attacks
poke3.attack(poke1)
poke3.attack(poke2)
