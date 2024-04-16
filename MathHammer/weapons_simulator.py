import random

class RangedWeapon:
    def __init__(self,
                 Name, Range, Attacks, Ballistic_Skill, Strength,
                 Armour_Penetration, Damage, Keywords=[]
                 ):
        self.N = Name
        self.R = Range
        self.A = Attacks
        self.BS = Ballistic_Skill
        self.S = Strength
        self.AP = Armour_Penetration
        self.D = Damage
        self.Keywords = Keywords

    def __str__(self):
        return f"Class Object of: {self.N}"


def shoot(weapon: RangedWeapon, printouts=False):
    hit_rolls = []
    for attacks in range(0, weapon.A):
        hit_rolls.append(random.randint(1, 6))

    if printouts:
        print("Original Hit rolls: " + str(hit_rolls))

    hits, crits = determine_hits(hit_rolls, weapon.BS)
    # Sustained Hits or Lethal Hits for example
    if printouts:
        print(hit_rolls)
        print(f"You landed {hits} hits, {crits} of which were crits!")
        if crits != 0:
            print(f"That's {hits + crits} total thanks to Sustained Hits X!")
    hits += handle_sustained_hits(crits, weapon.Keywords)

    wound_rolls = []
    for hit in range(0, hits):
        wound_rolls.append(random.randint(1, 6))

    if 1 in wound_rolls:
        wound_rolls = handle_slaughter(wound_rolls)

    if printouts:
        print("𓋹" * 20)
        print(f"Your {weapon.N} landed {hits} hits!")
        print(f"Wound rolls were: {wound_rolls}")
        print("𓋹" * 20)

    return wound_rolls, weapon.AP


def determine_hits(hit_rolls, ballistic_skill):
    hits = 0
    crit_hits = 0
    # crit_misses = 0
    for roll in hit_rolls:
        if roll >= ballistic_skill:
            hits += 1
        if roll == 6:
            crit_hits += 1
        # if roll == 1:
        #     crit_misses += 1

    return hits, crit_hits


def handle_sustained_hits(number_of_crits, rules):
    extra_hits = 0
    for rule in rules:
        if "Sustained Hits" in rule:
            # "Sustained Hits 3" would add 3 hits
            extra_hits += int(rule[-1]) * number_of_crits

    return extra_hits


def handle_slaughter(rolls_to_wound):
    number_of_rerolls = 0
    rerolls = []
    for roll in rolls_to_wound:
        if roll == 1:
            number_of_rerolls += 1
            rolls_to_wound.remove(roll)

    for reroll in range(0, number_of_rerolls):
        rerolls.append(random.randint(1, 6))


    new_wound_rolls = rolls_to_wound + rerolls
    return new_wound_rolls


def toughness_save_table(wound_rolls, weapon_ap, printout=False, toughness=0):


    if printout:
        print("Amongus")

    save_rolls = []
    for wound in wound_rolls:
        save_rolls.append(random.randint(1, 6))

    print(save_rolls)

    modified_save_rolls = [roll - 1 for roll in save_rolls]
    for save in save_rolls:
        if save == 1:
            modified_save_rolls.append(1)
        else:
            modified_save_rolls.append(save - 1)

    print(save_rolls)




def wound_successes(wound_rolls, weapon_strength=False, enemy_toughness = False, printouts=False):

    wounds_landed = []
    # print(wound_rolls)
    #
    # for requirement in range(2,7):
    #     print(f"Requirement: {requirement}")
    #     successes = 0
    #     for roll in wound_rolls:
    #         print(f"Roll: {roll}")
    #         if roll >= requirement:
    #             successes += 1
    #
    #     wounds_landed.append(successes)

    for value in range(2,7):
        # print(value)
        wounds_landed.append(sum(dice >= value for dice in wound_rolls))

    if printouts:
        print("Required Roll - Wounds Landed")
        print(f"      2+      -      {wounds_landed[0]}")
        print(f"      3+      -      {wounds_landed[1]}")
        print(f"      4+      -      {wounds_landed[2]}")
        print(f"      5+      -      {wounds_landed[3]}")
        print(f"      6+      -      {wounds_landed[4]}")

    if weapon_strength and enemy_toughness:
        # Produce the appropriate result
        if weapon_strength >= 2 * enemy_toughness:
            # 2+
            return wounds_landed[0]

        if weapon_strength > enemy_toughness:
            # 3+
            return wounds_landed[1]

        if weapon_strength == enemy_toughness:
            # 4+
            return wounds_landed[2]

        if weapon_strength < enemy_toughness:
            # 5+
            return wounds_landed[3]

        if weapon_strength <= 0.5 * enemy_toughness:
            # 6+
            return wounds_landed[4]

        return wounds_landed


    return wounds_landed


from collections import Counter

# bongletron = RangedWeapon("The Bongletron",20,2,2,6,4,3, "Sustained Hits 99")
exterminator = RangedWeapon("Enmitic Exterminator",
                            36,
                            6,
                            3,
                            6,
                            1,
                            1,
                            ["Heavy", "Rapid Fire 6", "Sustained Hits 1"])


flayer_claws = RangedWeapon(
    "Flayer Claws",
    0,
    4,
    3,
    4,
    1,
    1,
    ["Sustained Hits 1", "Twin-Linked"]
)

# wounds_rolled, ap = shoot(exterminator, True)
# wound_successes(wounds_rolled, printouts=True)
print("#"*20)
stabs, ap = shoot(flayer_claws, True)
wound_successes(stabs, printouts=True)
