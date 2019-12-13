#This is to try to modify a form fillable pdf
import os, pdfrw,PyPDF2,subprocess,webbrowser

data_dict={
    #top bar with character name and other char info
    #we will be having this character sheet start at level 1
    #Background, race, and class will be determined by user input and then verified with API
    "CharacterName":"TEST",
    "ClassLevel":"1",
    "Background":"TEST",
    "PlayerName":"TEST",
    "Race ":"TEST",
    "Alignment":"TEST",
    "XP":"0",

    #actual Stats and the stat modifiers.
    #modifiers are determined by the stats comparison to 10
    #if for example strength has a stat score of 17 the modifier will be +3 
    #the modifier is +- 1 for every 2 away from 10 so
    # stats = modifer
    # 1 = -4    (lowest possible score)
    # 2 = -4
    # 3 = -3
    # 4 = -3
    # 5 = -2
    # 6 = -2
    # 7 = -1
    # 8 = -1
    # 9 = 0
    # 10 = 0
    # 11 = 0
    # 12 = 1
    # 13 = 1
    # 14 = 2
    # 15 = 2
    # 16 = 3
    # 17 = 3
    # 18 = 4
    # 19 = 4
    # 20 = 4
    "STR":"TEST",
    "STRmod":"TEST",
    "DEX":"TEST",
    "DEXmod ":"TEST",
    "CON":"TEST",
    "CONmod":"TEST",
    "INT":"TEST",
    "INTmod":"TEST",
    "WIS":"TEST",
    "WISmod":"TEST",
    "CHA":"TEST",
    "CHamod":"TEST",

    #passive perception
    #TODO Figure out how this is calculated
    "Passive":"TEST",

    #other Proficiences and Languages box
    #determined by a combination of characters: race, class, and background
    "ProficienciesLang":"TESTTEST",

    #will remain 0 or empty as this is something the DM will awarded during game play
    "Inspiration":"TEST",

    #proficiency bonus
    #this will change as character levels up. 
    #I believe all characters start with a +2 at level one 
    #will confirm
    "ProfBonus":"+2",

    #Saving throws
    #these are dermined by combination of class, race, and background
    #if a saving throw has proficiency the the proficiencey bonus will be added to that skills ability modifier
    #ie if the character has a strength of 14 their ability modifier is +2 and if they are proficient at strength saving throws they add +2 for level 1
    #so the ST Strength line will read 4
    "Check Box 11":"Yes", #strength saving throw proficiency check box 
    "ST Strength":"TEST",
    "Check Box 18": "Yes",  # dexterity saving throw proficiency check box
    "ST Dexterity":"TEST",
    "Check Box 19": "Yes",   # Constitution saving throw proficiency check box
    "ST Constitution":"TEST",
    "Check Box 20": "Yes",  # Intelligence saving throw proficiency check box
    "ST Intelligence":"TEST",
    "Check Box 21": "Yes",  # wisdom saving throw proficiency check box
    "ST Wisdom":"TEST",
    "Check Box 22": "Yes",  # charisma saving throw proficiency check box
    "ST Charisma":"TEST",

    #skill checks these will be determined by a given skills stat modifier and if the character is profiecent in this skill the proficiency modifier will be added
    #ie if the character has a dexterity of 16 their ability modifier is +3 and if they are proficient at acrobatics they add +2 for level 1
    #so the acrobatics line will read 5
    "Check Box 23":"Yes", #acrobatic skill proficiency check box
    "Acrobatics":"TEST", 
    "Check Box 24": "Yes",  # animal handling skill proficiency check box
    "Animal":"TEST",
    "Check Box 25": "Yes",  # arcana skill proficiency check box
    "Arcana":"TEST",
    "Check Box 26": "Yes",  # athletics skill proficiency check box
    "Athletics":"TEST",
    "Check Box 27": "Yes",  # Deception skill proficiency check box
    "Deception ":"TEST",
    "Check Box 28": "Yes",  # history skill proficiency check box
    "History ":"TEST",
    "Check Box 29": "Yes",  # insight skill proficiency check box
    "Insight":"TEST",
    "Check Box 30": "Yes",  # Intimidation skill proficiency check box
    "Intimidation":"TEST",
    "Check Box 31": "Yes",   # Investigation skill proficiency check box
    "Investigation ":"TEST",
    "Check Box 32": "Yes",  # Medicine skill proficiency check box
    "Medicine":"TEST",
    "Check Box 33": "Yes",  # Nature skill proficiency check box
    "Nature":"TEST",
    "Check Box 34": "Yes",  # perception skill proficiency check box
    "Perception ":"TEST",
    "Check Box 35": "Yes",  # Performance skill proficiency check box
    "Performance":"TEST",
    "Check Box 36": "Yes",  # Persuassion skill proficiency check box
    "Persuasion":"TEST",
    "Check Box 37": "Yes",  # Religion skill proficiency check box
    "Religion":"TEST",
    "Check Box 38": "Yes",   # Slieght of Hand skill proficiency check box
    "SleightofHand":"TEST",
    "Check Box 39": "Yes",  # Stealth skill proficiency check box
    "Stealth ":"TEST",
    "Check Box 40": "Yes",  # Survival skill proficiency check box
    "Survival":"TEST",

    #character combat statistics 
    #Most of the time AC (Armor class is determined by dexterity modifier + level of armor)
    # will verify
    # Initiative is determined by dexterity modifier
    #Speed may be class dependent but will see if it is affected anywhere else
    #HPMax is determined by class and a stat will modify for proper logic
    #HP current and HP Temp will be left blank as those are only used during gameplay
    "AC":"TEST",
    "Initiative":"TEST",
    "Speed":"TEST",
    "HPMax":"TEST",
    "HPCurrent":"",
    "HPTemp":"",

    #Hit dice are determined by class and will change after level ups
    #will verify if they change the number you get based of class, race, or background but i believe it starts at 3
    "HDTotal":"TEST",
    "HD":"TEST",

    #Death Saving throws (successes and failures)
    #will remain blank is altered during gameplay
    #"Check Box 12":"No",
    #"Check Box 13":"No",
    #"Check Box 14":"No",
    #"Check Box 15":"No",
    #"Check Box 16":"No",
    #"Check Box 17":"No",

    #weapons and attack are determined by class and background 
    #The stats will be pulled from a seperate api call
    #Attack and Spellcasting text field will be filled in with special attack abilities from class, and race
    "Wpn Name":"TEST1",
    "Wpn1 AtkBonus":"TEST2",
    "Wpn1 Damage":"TEST3",
    "Wpn Name 2":"TEST4",
    "Wpn2 AtkBonus ":"TEST5",
    "Wpn2 Damage ":"TEST6",
    "Wpn Name 3":"TEST7",
    "Wpn3 AtkBonus  ":"TEST8",
    "Wpn3 Damage ":"TEST9",
    "AttacksSpellcasting":"TEST10",

    #currency tracker 
    #values will be determined from background
    "CP":"TEST",    #Copper
    "SP":"TEST",    #silver
    "EP":"TEST",    #electrum? will look up later most likely not needed for this program
    "GP":"TEST",    #Gold
    "PP":"TEST",    #Platinum
    "Equipment":"TEST", #will place equipment names here (Ie armor type, starting equipment packs)

    #Will allow user to enter custom information here as it has no bearing on stats
    "PersonalityTraits ":"TEST",
    "Ideals":"TEST",
    "Bonds":"TEST",
    "Flaws":"TEST",

    #Will contain some information from race, class, and backgrounds
    "Features and Traits":"TEST",
}

INVOICE_TEMPLATE_PATH = '.\\CharacterSheetTemplate.pdf'
INVOICE_OUTPUT_PATH = 'CharSheet.pdf'


ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'

def write_fillable_pdf(input_pdf_path, output_pdf_path, data_dict):
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    annotations = template_pdf.pages[0][ANNOT_KEY]
    for annotation in annotations:
        if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            if annotation[ANNOT_FIELD_KEY]:
                key = annotation[ANNOT_FIELD_KEY][1:-1]
                if key in data_dict.keys():
                    annotation.update(
                        pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                    )
                    annotation.update(pdfrw.PdfDict(AS=pdfrw.PdfName(str(data_dict[key]))))
    pdfrw.PdfWriter().write(output_pdf_path, template_pdf)

def main():
    write_fillable_pdf(INVOICE_TEMPLATE_PATH, INVOICE_OUTPUT_PATH, data_dict)
    '''charName = data_dict.get("CharacterName")
    #INVOICE_OUTPUT_PATH = charName + INVOICE_OUTPUT_PATH
    absPath = os.path.abspath(INVOICE_OUTPUT_PATH)
    absPath = "file://"+ absPath
    chrome=webbrowser
    chrome.open(absPath)'''
main()
