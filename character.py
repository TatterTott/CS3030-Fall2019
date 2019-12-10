class Character():
    def __init__(self):
        self.char_name = None
        self.char_class = None
        self.race = None
        self.background = None
        self.alignment = None
        self.player_name = None
        self.experience = 0
        self.personality = None
        self.ideals = None
        self.bonds = None
        self.flaws = None
        self.features = None
        self.traits = None
        self.str = None
        self.dex = None
        self.const = None
        self.int = None
        self.wisdom = None
        self.charisma = None
        self.str_modifier = None
        self.dex_modifier = None
        self.const_modifier = None
        self.int_modifier = None
        self.wisdom_modifier = None
        self.charisma_modifier = None
        self.inspiration = None
        self.passive_wisdom = None
        self.other_proficiencies = None
        self.languages = None
        self.equipment = []
        self.ability_bonuses = []   #strength, dexterity, constitution, intelligence, wisdom, charisma
        self.cp = None  #copper
        self.sp = None  #silver
        self.ep = None  #electrium
        self.gp = None  #gold
        self.pp = None  #platinum
        self.proficiency_bonus = None
        self.str_throw = None
        self.dex_throw = None
        self.const_throw = None
        self.int_throw = None
        self.wisdom_throw = None
        self.charisma_throw = None
        self.prof_skills = []
        self.prof_tools = []
        self.armor = None
        self.initiative = None
        self.speed = None
        self.HP_max = None
        self.hit_dice = None
        self.attacks = [] # 'NAME|ATTACK|DAMAGE'
