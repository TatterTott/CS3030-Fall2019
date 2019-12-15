
class StatCalculator():
    def update(character):
        skillProfs = character.ability_bonuses
        character.str = str(int(character.str) +int(skillProfs[0]))
        character.dex = str(int(character.dex) + int(skillProfs[1]))
        character.const = str(int(character.const) + int(skillProfs[2]))
        character.int = str(int(character.int) + int(skillProfs[3]))
        character.wisdom = str(int(character.wisdom) + int(skillProfs[4]))
        character.charisma = str(int(character.charisma) + int(skillProfs[5]))

        calculateModifiers(character)

        determineProfs(character)

        determineAC(character)

        character.HP_max = str(int(character.hit_dice) + int(character.const_modifier))

        weaponFiller(character)

def weaponFiller(character):
    numWeapons = len(character.weapon_dict)

    if numWeapons >= 3:
        weapon1Stat = str(character.weapon_dict.get(list(character.weapon_dict)[0])[0]) + "d" + str(character.weapon_dict.get(list(character.weapon_dict)[0])[1])
        character.weapons[list(character.weapon_dict)[0]] = weapon1Stat

        weapon2Stat = str(character.weapon_dict.get(list(character.weapon_dict)[1])[0]) + "d" + str(character.weapon_dict.get(list(character.weapon_dict)[1])[1])
        character.weapons[list(character.weapon_dict)[1]] = weapon2Stat

        weapon3Stat = str(character.weapon_dict.get(list(character.weapon_dict)[2])[0]) + "d" + str(character.weapon_dict.get(list(character.weapon_dict)[2])[1])
        character.weapons[list(character.weapon_dict)[2]] = weapon3Stat

    elif numWeapons == 2:
        weapon1Stat = str(character.weapon_dict.get(list(character.weapon_dict)[0])[
                          0]) + "d" + str(character.weapon_dict.get(list(character.weapon_dict)[0])[1])
        character.weapons[list(character.weapon_dict)[0]] = weapon1Stat

        weapon2Stat = str(character.weapon_dict.get(list(character.weapon_dict)[1])[
                          0]) + "d" + str(character.weapon_dict.get(list(character.weapon_dict)[1])[1])
        character.weapons[list(character.weapon_dict)[1]] = weapon2Stat

        character.weapons[""] = ""

    elif numWeapons == 1:
        weapon1Stat = str(character.weapon_dict.get(list(character.weapon_dict)[0])[
                          0]) + "d" + str(character.weapon_dict.get(list(character.weapon_dict)[0])[1])
        character.weapons[list(character.weapon_dict)[0]] = weapon1Stat

        character.weapons[""] = ""

        character.weapons[" "] = ""
        

def calculateModifiers(character):
    strSkill = int(character.str)
    dexSkill = int(character.dex)
    conSkill = int(character.const)
    intSkill = int(character.int)
    wisSkill = int(character.wisdom)
    charSkill = int(character.charisma)

    character.str_modifier = calcMod(strSkill)
    character.dex_modifier = calcMod(dexSkill)
    character.const_modifier = calcMod(conSkill)
    character.int_modifier = calcMod(intSkill)
    character.wisdom_modifier = calcMod(wisSkill)
    character.charisma_modifier = calcMod(charSkill)


def calcMod(skill):
    val = int((skill - 10) / 2)
    return(val)

def determineAC(character):
    listEquip = []
    for item in character.startingEquipment:
        listEquip.append(item[0])
    
    if "Leather" in listEquip:
        character.armor = str(11 + int(character.dex_modifier))
    if "Chain" in listEquip:
        character.armor = str(13 + int(character.dex_modifier))
    if "Plate" in listEquip:
        character.armor = "18"
    else:
        character.armor = str(10 + int(character.dex_modifier))

    if character.char_class == "Monk":
        character.armor = str(10 + int(character.dex_modifier) + int(character.wisdom_modifier))
    elif character.char_class == "Barbarian":
        character.armor = str(
            10 + int(character.dex_modifier) + int(character.const_modifier))

def determineProfs(character):
    if character.saving_throws.get("STR") == "No":
        character.str_throw = character.str_modifier
    else:
        character.str_throw = str(int(character.str_modifier) + int(character.proficiency_bonus))

    if character.saving_throws.get("DEX") == "No":
        character.dex_throw = character.dex_modifier
    else:
        character.dex_throw = str(int(character.dex_modifier) + int(character.proficiency_bonus))

    if character.saving_throws.get("CON") == "No":
        character.const_throw = character.const_modifier
    else:
        character.const_throw = str(int(character.const_modifier) + int(character.proficiency_bonus))

    if character.saving_throws.get("INT") == "No":
        character.int_throw = character.int_modifier
    else:
        character.int_throw = str(int(character.int_modifier) + int(character.proficiency_bonus))

    if character.saving_throws.get("WIS") == "No":
        character.wisdom_throw = character.wisdom_modifier
    else:
        character.wisdom_throw = str(int(character.wisdom_modifier) + int(character.proficiency_bonus))

    if character.saving_throws.get("CHA") == "No":
        character.charisma_throw = character.charisma_modifier
    else:
        character.charisma_throw = str(int(character.charisma_modifier) + int(character.proficiency_bonus))


    for skill in character.prof_skills:
        if character.prof_skills[skill] == "Yes":
            character.skills[skill] = character.proficiency_bonus
        else:
            character.skills[skill] = "0"

    modifier = character.str_modifier
    character.skills['Athletics'] = str(int(character.skills['Athletics']) + int(modifier))

    modifier = character.dex_modifier
    character.skills['Acrobatics'] = str(int(character.skills['Acrobatics']) + int(modifier))
    character.skills['Slieght of hand'] = str(int(character.skills['Sleight of hand']) + int(modifier))
    character.skills['Stealth'] = str(int(character.skills['Stealth']) + int(modifier))

    modifier = character.int_modifier
    character.skills['Arcana'] = str(int(character.skills['Arcana']) + int(modifier))
    character.skills['History'] = str(int(character.skills['History']) + int(modifier))
    character.skills['Investigation'] = str(int(character.skills['Investigation']) + int(modifier))
    character.skills['Nature'] = str(int(character.skills['Nature']) + int(modifier))
    character.skills['Religion'] = str(int(character.skills['Religion']) + int(modifier))

    modifier = character.wisdom_modifier
    character.skills['Animal Handling'] = str(int(character.skills['Animal Handling']) + int(modifier))
    character.skills['Insight'] = str(int(character.skills['Insight']) + int(modifier))
    character.skills['Medicine'] = str(int(character.skills['Medicine']) + int(modifier))
    character.skills['Perception'] = str(int(character.skills['Perception']) + int(modifier))
    character.skills['Survival'] = str(int(character.skills['Survival']) + int(modifier))

    modifier = character.charisma_modifier
    character.skills['Deception'] = str(int(character.skills['Deception']) + int(modifier))
    character.skills['Intimidation'] = str(int(character.skills['Intimidation']) + int(modifier))
    character.skills['Performance'] = str(int(character.skills['Performance']) + int(modifier))
    character.skills['Persuasion'] = str(int(character.skills['Persuasion']) + int(modifier))

    character.passive_wisdom = str(10 + int(character.skills.get("Perception")))

    character.initiative = character.dex_modifier
    
