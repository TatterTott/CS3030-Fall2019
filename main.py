from character import Character
from menu import Menu
import PDFWriter

#main is intended to be left as short as possible, all logic should be handled in
#class instances that we make to fill in character sheet variables
if __name__ == '__main__':
    #creates menu class
    menu = Menu()
    #shows main menu to user
    menu.menuOption()
    #creates an instance the character
    character = Character()
    #this method will handle filling in the character variables
    menu.buildCharacterSheet(character)

