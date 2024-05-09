print("Chapter 5 - If Statements")
# If I practice, I get better
print("-"*25)

my_number = 3
if my_number > 5:
    print("It's over 5")
else:
    print("It's 5 or less")

cars_driven = ["renault", "suzuki", "mercedes"]
if "rolls royce" in cars_driven:
    print("Yippee!")
else:
    print("Can't retire just yet.")

import random
alien_colours = ["red","blue","gold"]
shot_alien = alien_colours[random.randint(0,2)]

if shot_alien == "red":
    print(f"You scored 5 points for shooting that {shot_alien.upper()}"
          f" alien!")
elif shot_alien == "blue":
    print(f"Nice one! That {shot_alien.upper()} alien was worth"
          f" 50 points!")
elif shot_alien == "gold":
    print(f"INCREDIBLE! The legendary {shot_alien.upper()} alien"
          f" was worth 1,000,000 points!")
