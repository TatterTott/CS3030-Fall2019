
class StatCalculator():
    def update(character):
        skillProfs = character.ability_bonuses
        character.str = str(int(character.str) +int(skillProfs[0]))
        dex = str(int(character.dex) + int(skillProfs[1]))
        cons = str(int(character.const) + int(skillProfs[2]))
        intel = str(int(character.int) + int(skillProfs[3]))
        wis = str(int(character.wisdom) + int(skillProfs[4]))
        charisma = str(int(character.charisma) + int(skillProfs[5]))

        calculateModifiers(character)

        determineProfs(character)

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

def determineProfs(character):
    for skill in character.prof_skills:
        if character.prof_skills[skill] == "Yes":
            character.skills[skill] = character.proficiency_bonus
        else:
            character.skills[skill] = "0"

    for key in character.prof_skills:
        pass
        #TODO add skills
        #print(key,character.prof_skills.get(key))

    for key in character.skills:
        pass
        #print(key, character.skills.get(key))

    '''character.prof_skills['Acrobatics']
    character.prof_skills['Animal Handling']
    character.prof_skills['Arcana']
    character.prof_skills['Athletics']
    character.prof_skills['Deception']
    character.prof_skills['History']
    character.prof_skills['Insight']
    character.prof_skills['Intimidation']
    character.prof_skills['Investigation']
    character.prof_skills['Medicine']
    character.prof_skills['Nature']
    character.prof_skills['Perception']
    character.prof_skills['Performance']
    character.prof_skills['Persuasion']
    character.prof_skills['Religion']
    character.prof_skills['Sleight of hand']
    character.prof_skills['Stealth']
    character.prof_skills['Survival']'''

