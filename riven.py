from random import choice, randint, sample

# Different polarities rivens can have
polarities = ["Madurai", "Vazarin", "Naramon"]

# Different weapon types
riven_types = ["Archgun", "Companion", "Melee", "Pistol", "Rifle", "Kitgun", "Zaw", "Shotgun"]

# Dictionary with all riven attributes. Includes attribute prefix, core, and suffix
riven_attributes = {
    "Combo Count Chance" : ["Laci", "Nus"],
    "Ammo Maximum" : ["Ampi", "Bin"],
    "Damage vs. Corpus" : ["Manti", "Tron"],
    "Damage vs. Grineer" : ["Argi", "Con"],
    "Damage vs. Infested" : ["Pura", "Ada"],
    "Cold Damage" : ["Geli", "Do"],
    "Combo Duration" : ["Tempi", "Nem"],
    "Critical Chance" : ["Crita", "Cron"],
    "Critical Chance on Slide Attack" : ["Pleci", "Nent"],
    "Critical Damage" : ["Acri", "Tis"],
    "Base Damage / Melee Damage" : ["Visi", "Ata"],
    "Electric Damage" : ["Vexi", "Tio"],
    "Heat Damage" : ["Igni", "Pha"],
    "Finisher Damage" : ["Exi", "Cta"],
    "Fire Rate / Attack Speed" : ["Chroni", "Dra"],
    "Flight Speed" : ["Conci", "Nak"],
    "Initial Combo" : ["Para", "Um"],
    "Impact Damage" : ["Magna", "Ton"],
    "Magazine Capacity" : ["Arma", "Tin"],
    "Melee Combo Efficiency" : ["Forti", "Us"],
    "Multishot" : ["Sati", "Can"],
    "Toxin Damage" : ["Toxi", "Tox"],
    "Punch Through" : ["Lexi", "Nok"],
    "Puncture Damage" : ["Insi", "Cak"],
    "Reload Speed" : ["Feva", "Tak"],
    "Range" : ["Locti", "Tor"],
    "Slash Damage" : ["Sci", "Sus"],
    "Status Chance" : ["Hexa", "Dex"],
    "Status Duration" : ["Deci", "Des"],
    "Recoil" : ["Zeti", "Mag"],
    "Zoom" : ["Hera", "Lis"]
    }

melee_only_attributes = ["Combo Count Chance", "Combo Duration", "Critical Chance on Slide Attack", "Finisher Damage", "Initial Combo", "Melee Combo Efficiency", "Range"]

gun_only_attributes = ["Ammo Maximum", "Magazine Capacity", "Multishot", "Reload Speed", "Recoil", "Zoom"]

def riven_sim(x):
    # Create temp dictionary for use
    temp = riven_attributes.copy()
    # Coin flip if it will have a negative attribute
    negative_attribute = bool(randint(0,1))
    # For melee mods
    if x == "Melee":
        # Take out all gun attributes
        for key in gun_only_attributes: del(temp[key])
        # Choose 2-4 attributes (Withouth replacement)
        riven = sample(list(temp.items()), randint(2,4))
        # If there are 4 attributes, Last one is negative; If two, none can be negative
        if(len(riven) == 4):
            negative_attribute = True
        if(len(riven)==2):
            negative_attribute = False
    # For non-melee mods
    else:
        # Take out all melee attributes
        for key in melee_only_attributes: del(temp[key])
        # Choose 2-4 attributes (Without replacement)
        riven = sample(list(temp.items()), randint(2,4))
        # If there are 4 attributes, Last one is negative; If two, none can be negative
        if len(riven) == 4:
            negative_attribute = True
        if len(riven) == 2:
            negative_attribute = False
    # Returns riven information
    riven.append(negative_attribute)
    return riven

def print_riven(riven):
    # Print Polarities
    polarity = choice(polarities)
    if polarity == 'Naramon':
        print(u'\u29ff')
    elif polarity == 'Vazarin':
        print(u'\u25f9')
    else:
        print(u'\u2a57')
    # Print Riven Name
    if not riven[-1]:
        if len(riven) == 4:
             print(riven[0][1][0] + "-" + riven[1][1][0] + riven[2][1][1])
        else:
             print(riven[0][1][0] + riven[1][1][1])
    else:
         if len(riven) == 5:
            print(riven[0][1][0] + "-" + riven[1][1][0] + riven[2][1][1])
         else:
            print(riven[0][1][0] + riven[1][1][1])
    # Print Attributes of Riven
    if riven[-1]:
        for i in riven[:-2]:
            print("+" + i[0])
        print("-" + riven[-2][0])
    else:
        for i in riven[:-1]:
            print("+" + i[0])

def desirable_riven(type, des_att=None):
    att_list = []
    scores = {
        'Score 0' : 0,
        'Score 1' : 0,
        'Score 2' : 0,
        'Score 3' : 0,
        'Score 4' : 0
    }
    print('Enter desirable attributes or hit enter to finish')
    while (des_att := input()) != '':
        att_list.append(des_att)
    for x in range(1000000):
        s = 0
        created_riven = riven_sim(type)
        if created_riven[-1]:
            for i in created_riven[:-2]:
                if i[0] in att_list:
                    s+=1
            if created_riven[-2][0] in att_list:
                s-=1
            else:
                s+=1
        else:
            for i in created_riven[:-1]:
                if i[0] in att_list:
                    s+=1
        if s < 0:
            s = 0
        scores['Score ' + str(s)] += 1
    print(scores)

def riven_probability(x):
    # For Score 4
    prob = 4 * (1/3) * (1/2) * (x/31) * ((x-1)/30) * ((x-2)/29) * ((28-(x-3))/28)
    return prob

# Main method
if __name__ == "__main__":
    type = input(u'\u26f9' + " Enter weapon type: ")
    desirable_riven(type)
    print(riven_probability(4))
