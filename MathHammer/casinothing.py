
result_string = "000434320004030023002000400320030203020000303200004444000400000000000000003"
results = []

for result in range(0, len(result_string)):
    results.append(int(result_string[result]) - 1)

# print(results)
# print(sum(results))

# stakes = [5,10,25,50,100,250,500,1000,2500,5000,10000]
stakes = [5,10,20,40,80,160,320,625,1250,2500,5000,10000]

import random
def spin_the_wheel(stake:int, probabilities:list = [40,30,20,10], printouts:bool = False) -> int:
    roll = random.randint(0,100)
    if sum(probabilities) != 100:
        raise ValueError("These probabilities do not sum to 100%!")
        return False

    if roll < probabilities[0]:
        if printouts: print(f"You lose! -{stake}")
        return -stake
    elif roll < (probabilities[0] + probabilities[1]):
        if printouts: print(f"You won 2x! +{stake}")
        return stake
    elif roll < (probabilities[0] + probabilities[1] + probabilities[2]):
        if printouts: print(f"You won 3x! +{2 * stake}")
        return 2*stake
    elif roll <= 100:
        if printouts: print(f"You won 4x! +{3 * stake}")
        return 3*stake
    else:
        if printouts: print("Whoops! This code shouldn't happen!")
        return 0
    return 0


def simulate_gambling(starting_balance:int, stake_per_spin:int, spins, printouts = False):
    balance = starting_balance
    for spin in range(0,spins):
        balance += spin_the_wheel(stake_per_spin)

    if printouts: print(f"Final balance from simulation: {balance}")
    return balance



balance = 1000
gamble_amount = 100
results = []
for i in range(0,1000):
    results.append(simulate_gambling(balance, gamble_amount, 10000))

print(sum(results)/len(results))
for x in results:
    if x < 0:
        print("LOSER DETECTED")




