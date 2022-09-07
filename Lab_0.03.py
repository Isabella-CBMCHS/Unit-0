'''
##############
## Lab 0.03 ##
##############

Instructions:
-------------
1.  Finish writing the __add__ method for the time class from the Do Now.

2.  Write a definition for a class named Kangaroo with the following methods:

    An __init__ method that initializes an attribute named pouch_contents to an empty list.

    A method named put_in_pouch that takes an object of any type and adds it to pouch_contents.

    A __str__ method that returns a string representation of the Kangaroo object and the contents of the pouch.


Tips to give students:
----------------------
- This exercise is a cautionary tale about one of the most common, and difficult to find, errors in Python

- TypeError: Can't convert 'list' object to str implicitly

- Use the str() function to convert the list object to a string.

- Test your code by creating two Kangaroo objects

    assign them to variables named kanga and roo

    add roo to the contents of kanga's pouch

class Kangaroo():
    def __init__(self, name):
        self.name = name
        self.pouch_contents = []

    def put_in_pouch(self, object):
        self.pouch_contents.append(object)

    def __str__(self):
        return f"{self.name} is a kangaroo with {self.pouch_contents} in its pouch."

kanga_test = Kangaroo("Kanga")
kanga_two = Kangaroo("Roo")

kanga_test.put_in_pouch("baby kangaroo")
kanga_test.put_in_pouch("apple")

kanga_test.put_in_pouch(kanga_two)
print(kanga_test)

Extra Credit
------------
Return to your Pet class from Lab 7.02. Research the isinstance function to write a method, 
is_friend that will take in another pet and return True if the two pets are friends, and 
false if they are not.

Rules:
------
- If they are both dogs they are friends.

- If the instance is a dog and the other pet is a cat, they are friends.

- If the instance is a cat and the other is a dog they are not friends.

- If they are both cats they are not friends.
'''

class Pet():
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def is_friend(self, other):
        # if dog and dog
        if isinstance(self, Dog) and isinstance(other, Dog):
            return f"{self.name} and {other.name} are friends"
        # if dog and cat
        if isinstance(self, Dog) and isinstance(other, Cat):
            return f"{self.name} and {other.name} are friends"
        #  if cat and dog
        if isinstance(self, Cat) and isinstance(other, Dog):
            return f"{self.name} and {other.name} are not friends"
        # if cat and cat
        if isinstance(self, Cat) and isinstance(other, Cat):
            return f"{self.name} and {other.name} are not friends"
        

class Dog(Pet):
    food = "kibble"
    noise = "woof"

class Cat(Pet):
    food = "fish"
    noise = "meow"

class Fish(Pet):
    food = "seaweed"
    noise = "blub blub"

class Snake(Pet):
    food = "mice"
    noise = "hiss"

def pet_info(list_of_pets):
    for pet in list_of_pets:
        print(f"{pet.name} eats {pet.food}.")

pet1 = Dog('brown', 'Buddy')
pet2 = Cat('black', 'Lucky')
pet3 = Fish('orange', 'Goldie')
pet4 = Snake('white', 'Snowy')
pet5 = Dog('white', 'John')
pet6 = Cat('orange', 'Tabitha')

PET_LIST = [pet1, pet2, pet3, pet4]

# dog and dog
print(pet1.is_friend(pet5))

# cat and cat
print(pet2.is_friend(pet6))

# dog and cat
print(pet5.is_friend(pet2))

# cat and dog
print(pet6.is_friend(pet1))

# cat and cat
<<<<<<< HEAD
print(pet2.is_friend(pet6))
=======
print(pet2.is_friend(pet6))
>>>>>>> 5dd4fdefa1c09d4237602db83fb63870db2138f0
