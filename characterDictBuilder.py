
class CharacterDictBuilder():
    def builder(character):
        charDict = {}
        charDict['CharacterName'] = character.char_name
        charDict['ClassLevel'] = character.char_class
        charDict['Background'] = character.background
        charDict['PlayerName'] = character.player_name
        charDict['Race '] = character.race
        charDict['Alignment'] = ""
        charDict['XP'] = 0

        charDict['STR'] = character.str
        charDict['STRmod'] = character.str_modifier
        charDict['DEX'] = character.dex
        charDict['DEXmod '] = character.dex_modifier
        charDict['CON'] = character.const
        charDict['CONmod'] = character.const_modifier
        charDict['INT'] = character.int
        charDict['INTmod'] = character.int_modifier
        charDict['WIS'] = character.wisdom
        charDict['WISmod'] = character.wisdom_modifier
        charDict['CHA'] = character.charisma
        charDict['CHamod'] = character.charisma_modifier

        charDict['Passive'] = "FIX"

        profsString = ', '.join(str(i) for i in character.prof_misc)
        charDict['ProficienciesLang'] = profsString

        charDict['Inspiration'] = ""

        charDict['ProfBonus'] = "+2"

        #charDict['Check Box 11'] = character.saving_throws.get('STR')
        charDict['ST Strength'] = character.str_throw
        #charDict['Check Box 18'] = character.saving_throws.get("DEX")
        charDict['ST Dexterity'] = character.dex_throw
        #charDict['Check Box 19'] = character.saving_throws.get('CON')
        charDict['ST Constitution'] = character.const_throw
        #charDict['Check Box 20'] = character.saving_throws.get('INT')
        charDict['ST Intelligence'] = character.int_throw
        #charDict['Check Box 21'] = character.saving_throws.get('WIS')
        charDict['ST Wisdom'] = character.wisdom_throw
        #charDict['Check Box 22'] = character.saving_throws.get('CHA')
        charDict['ST Charisma'] = character.charisma_throw

        #charDict['Check Box 23'] = character.prof_skills.get("Acrobatics")
        charDict['Acrobatics'] = character.skills.get('Acrobatics')
        #charDict['Check Box 24'] = character.prof_skills.get("Animal Handling")
        charDict['Animal'] = character.skills.get('Animal Handling')
        #charDict['Check Box 25'] = character.prof_skills.get("Arcana")
        charDict['Arcana'] = character.skills.get('Arcana')
        #charDict['Check Box 26'] = character.prof_skills.get("Athletics")
        charDict['Athletics'] = character.skills.get('Athletics')
        #charDict['Check Box 27'] = character.prof_skills.get("Deception")
        charDict['Deception'] = character.skills.get('Deception')
        #charDict['Check Box 28'] = character.prof_skills.get("History")
        charDict['History'] = character.skills.get('History')
        #charDict['Check Box 29'] = character.prof_skills.get("Insight")
        charDict['Insight'] = character.skills.get('Insight')
        #charDict['Check Box 30'] = character.prof_skills.get("Intimidation")
        charDict['Intimidation'] = character.skills.get('Intimidation')
        #charDict['Check Box 31'] = character.prof_skills.get("Investigation")
        charDict['Investigation'] = character.skills.get('Investigation')
        #charDict['Check Box 32'] = character.prof_skills.get("Medicine")
        charDict['Medicine'] = character.skills.get('Medicine')
        #charDict['Check Box 33'] = character.prof_skills.get("Nature")
        charDict['Nature'] = character.skills.get('Nature')
        #charDict['Check Box 34'] = character.prof_skills.get("Perception")
        charDict['Perception'] = character.skills.get('Perception')
        #charDict['Check Box 35'] = character.prof_skills.get("Performance")
        charDict['Performance'] = character.skills.get('Performance')
        #charDict['Check Box 36'] = character.prof_skills.get("Persuasion")
        charDict['Persuasion'] = character.skills.get('Persuasion')
        #charDict['Check Box 37'] = character.prof_skills.get("Religion")
        charDict['Religion'] = character.skills.get('Religion')
        #charDict['Check Box 38'] = character.prof_skills.get("Sleight of hand")
        charDict['SleightofHand'] = character.skills.get('Sleight of hand')
        #charDict['Check Box 39'] = character.prof_skills.get("Stealth")
        charDict['Stealth'] = character.skills.get('Stealth')
        #charDict['Check Box 40'] = character.prof_skills.get("Survival")
        charDict['Survival'] = character.skills.get('Survival')
        
        charDict['AC'] = character.armor
        charDict['Initiative'] = character.initiative
        charDict['Speed']= character.speed
        charDict['HPMax'] = character.HP_max
        charDict['HPCurrent'] = ''
        charDict['HPTemp'] = ''

        charDict["HDTotal"] = "1d"+str(character.hit_dice)
        charDict['HD'] = ""

        #charDict['Wpn Name'] = list(character.weapons)[0]
        #charDict['Wpn1 AtkBonus'] = character.weapons.get(list(character.weapons)[0])[0]
        #charDict['Wpn1 Damage'] = character.weapons.get(list(character.weapons)[0])[1]
        #charDict['Wpn Name 2'] = list(character.weapons)[1]
        #charDict['Wpn2 AtkBonus '] = character.weapons.get(list(character.weapons)[1])[0]
        #charDict['Wpn1 Damage '] = character.weapons.get(list(character.weapons)[1])[1]
        #charDict['Wpn Name 3'] = list(character.weapons)[2]
        #charDict['Wpn3 AtkBonus  '] = character.weapons.get(list(character.weapons)[2])[0]
        #charDict['Wpn3 Damage '] = character.weapons.get(list(character.weapons)[2])[1]

        charDict["CP"] = character.cp
        charDict['SP'] = character.sp
        charDict["EP"] = character.ep
        charDict['GP'] = character.gp
        charDict["PP"] = character.pp
        equipment = ""
        for elem in character.equipment:
            equipment += '-'+str(elem) +"\n"
        charDict['Equipment'] = equipment

        charDict['PersonalityTraits '] = character.personality
        charDict['Ideals'] = character.ideals
        charDict['Bonds'] = character.bonds
        charDict['Flaws'] = character.flaws

        charDict["Features and Traits"] = character.traits

        return charDict
