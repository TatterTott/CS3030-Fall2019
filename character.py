class Character():
    def __init__(self):
        self.char_name = ""
        self.char_class = ""
        self.race = ""
        self.background = ""
        self.alignment = ""
        self.player_name = ""
        self.experience = ""
        self.personality = ""
        self.ideals = ""
        self.bonds = ""
        self.flaws = ""
        self.features = ""
        self.traits = ""
        self.str = ""
        self.dex = ""
        self.const = ""
        self.int = ""
        self.wisdom = ""
        self.charisma = ""
        self.str_modifier = ""
        self.dex_modifier = ""
        self.const_modifier = ""
        self.int_modifier = ""
        self.wisdom_modifier = ""
        self.charisma_modifier = ""
        self.inspiration = ""
        self.passive_wisdom = ""
        self.other_proficiencies = ""
        self.languages = []
        self.equipment = []
        self.startingEquipment = []
        self.ability_bonuses = []   #strength, dexterity, constitution, intelligence, wisdom, charisma
        self.cp = ""  #copper
        self.sp = ""  #silver
        self.ep = ""  #electrium
        self.gp = ""  #gold
        self.pp = ""  #platinum
        self.proficiency_bonus = "2"
        self.str_throw = ""
        self.dex_throw = ""
        self.const_throw = ""
        self.int_throw = ""
        self.wisdom_throw = ""
        self.charisma_throw = ""
        self.saving_throws = {'STR':'No','DEX':'No','CON':'No','INT':'No','WIS':'No','CHA':'No'}
        self.skills = {'Acrobatics': '',
                       'Animal Handling': '',
                       'Arcana': '',
                       'Athletics': '',
                       'Deception': '',
                       'History': '',
                       'Insight': '',
                       'Intimidation': '',
                       'Investigation': '',
                       'Medicine': '',
                       'Nature': '',
                       'Perception': '',
                       'Performance': '',
                       'Persuasion': '',
                       'Religion': '',
                       'Sleight of hand': '',
                       'Stealth': '',
                       'Survival': '',
                       }
        self.prof_skills = {'Acrobatics': 'No',
                            'Animal Handling': 'No',
                            'Arcana': 'No',
                            'Athletics': 'No',
                            'Deception': 'No',
                            'History': 'No',
                            'Insight': 'No',
                            'Intimidation': 'No',
                            'Investigation': 'No',
                            'Medicine': 'No',
                            'Nature': 'No',
                            'Perception': 'No',
                            'Performance': 'No',
                            'Persuasion': 'No',
                            'Religion': 'No',
                            'Sleight of hand': 'No',
                            'Stealth': 'No',
                            'Survival': 'No',
                            }
                            
        self.prof_misc = []
        self.armor = ""
        self.initiative = ""
        self.speed = ""
        self.HP_max = ""
        self.hit_dice = ""
        self.weapon_dict = {} #{weaponName:(dict_count,dice_value)}
        #self.weapons = {} # {wpn1:[atk bonus, damage],wpn2:[atk bonus, damage],...}
