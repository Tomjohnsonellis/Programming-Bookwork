class Unit:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.stats = {
            "M": 8,
            "T": 6,
            "Sv":3,
            "W":4,
            "Ld":7,
            "OC":2
        }
        self.ranged_weapons = [
            {
                "Name":"Enmitic Exterminator",
                "R":36,
                "A":6,
                "BS":3,
                "S":6,
                "AP":1,
                "D":1,
                "Keywords":["Heavy","Rapid Fire 6","Sustained Hits 1"]
            }
        ]
        self.melee_weapons = []


    def __str__(self):
        return f"Class Object of: {self.name}"

friendly_men = Unit("Lokhust Heavy Destroyers", 2)
print(friendly_men)
print(friendly_men.stats["M"])
print(friendly_men.ranged_weapons[0]["Name"])

import random as rng
def rolldice(amount=1):
    rolls = []
    for x in range(0,amount):
        rng.seed()
        rolls.append(rng.randint(1, 6))

    return rolls

print(rolldice(5))

# Example for Lokhust Heavy Destroyers
LHD = Unit("Lokhust Heavy Destroyers", 2)
# Assume they are shooting at something in range
for model in range(0, ):
    shoot()

def simulate_shooting_phase(some_unit):
    for model in range(0,some_unit.size):
        shoot(some_unit.ranged_weapon[0])


def shoot(weapon_profile:dict):
    shooting_results = []
    hits = 0
    wounds = 0
    # Roll dice for each attack
    rolls = rolldice(weapon_profile["A"])
    # Determine what crit/hit
    for roll in rolls:
        if roll == 6:
            hits += 2
            continue
        if roll >= weapon_profile["BS"]:
            hits += 1

    hits = determine_hits(ballistic_skill)

determine_hits(rolls, ballistic_skill)

