import random

class StatRoller():
    def rollForStats(character):
        shouldRoll = input("Would you like the program to randomly roll your stats?").lower()
        if shouldRoll == "yes":
            roller(character)
            '''badRoll= True
            while badRoll:
                isGood = input("Is this an acceptable roll? ").lower()
                if isGood == "yes":
                    badRoll = False
                roller(character)'''
        elif (shouldRoll == 'no'):
            enterStats(character)
        else:
            print("Unexpected Response: generating randomized stats.")
            roller(character) 


def roller(character):
    character.str = random.randint(1, 20)
    character.dex = random.randint(1, 20)
    character.const = random.randint(1, 20)
    character.int = random.randint(1, 20)
    character.wisdom = random.randint(1, 20)
    character.charisma = random.randint(1, 20)
    print("Strength", character.str)
    print("Dexterity", character.dex)
    print("Constitution", character.const)
    print("Intelligence", character.int)
    print("Wisdom", character.wisdom)
    print("Charisma", character.charisma)

def enterStats(character):
    character.str = input("Please enter characters Strength: ")
    character.dex = input("Please enter characters Dexterity: ")
    character.const = input("Please enter characters Constitution: ")
    character.int = input("Please enter characters Intelligence: ")
    character.wisdom = input("Please enter characters Wisdom: ")
    character.charisma = input("Please enter characters Charisma: ")
    print("Strength", character.str)
    print("Dexterity", character.dex)
    print("Constitution", character.const)
    print("Intelligence", character.int)
    print("Wisdom", character.wisdom)
    print("Charisma", character.charisma)
