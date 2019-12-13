
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
    skillProfs = character.prof_skills
    for skill in character.skills:
        if skill in skillProfs:
            pass

