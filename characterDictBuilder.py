
class CharacterDictBuilder():
    charDict={}
    def builder(character):
        charDict['CharacterName'] = character.char_name
        charDict['ClassLevel'] = "1"
        charDict['Background'] = character.background
        charDict['PlayerName'] = character.player_name
        charDict['Race'] = character.race
        charDict['Alignment'] = ""
        charDict['XP'] = 0

        charDict['STR'] = character.str
        charDict['STRmod'] = character.str_mod
        charDict['DEX'] = character.dex
        charDict['DEXmod'] = character.dex_mod
        charDict['CON'] = character.const
        charDict['CONmod'] = character.const_mod
        charDict['INT'] = character.int
        charDict['INTmod'] = character.int_mod
        charDict['WIS'] = character.wis
        charDict['WISmod'] = character.wisdom_mod
        charDict['CHA'] = character.charisma
        charDict['CHamod'] = character.charisma_mod

        charDict['Passive'] = "FIX"

        charDict['ProficienciesLang'] = "NON SKILL PROFS" 

        charDict['Inspiration'] = ""

        charDict['ProfBonus'] = "+2"

        charDict['Check Box 11'] = character.str_throw
        

        