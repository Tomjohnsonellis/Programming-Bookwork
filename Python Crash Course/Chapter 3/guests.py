# Chapter 3 ends with some exercises to do, themed around dinner guests
# Ex 3-4: Make a list of 3 guests, then print a message to invite each person to dinner
dinner_guests = ["adam", "bill", "cindy"]
print("Good evening " + dinner_guests[0].title() + ", you are invited to dinner at my abode at 123 Town Street.")
print("Good evening " + dinner_guests[1].title() + ", you are invited to dinner at my abode at 123 Town Street.")
print("Good evening " + dinner_guests[2].title() + ", you are invited to dinner at my abode at 123 Town Street.")

# Ex 3-5: One of your guests can't make it!
# 1) print out who can't attend
# 2) replace their name in the list with a new guest,
# 3) print out a new set of invitations
print(25 * "-")
print("Sadly, " + dinner_guests[1].title() + " is unable to attend!")
dinner_guests[1] = "Daniella"
print("Good evening " + dinner_guests[0].title() + ", you are invited to dinner at my abode at 123 Town Street.")
print("Good evening " + dinner_guests[1].title() + ", you are invited to dinner at my abode at 123 Town Street.")
print("Good evening " + dinner_guests[2].title() + ", you are invited to dinner at my abode at 123 Town Street.")

# Ex 3-6: You have found a bigger table, and so can host more guests!
# 1) print out a message to inform everyone
# 2) use .insert() to add a new guest at the beginning of the list
# 3) use .insert() to add a new guest at the middle of the list
# 4) use .append() to add a new guest to the end of the list
# 5) print out new invitations, one for each guest
print(25 * "-")
print("Attention dinnermates, I have located a larger dinner table and so will be expanding the guest list.")
dinner_guests.insert(0,"Zidane")
dinner_guests.insert(2,"Yuffie") # index 1 would also be in the middle of this 4 item list
dinner_guests.append("Vivi")
print("Greetings " + dinner_guests[0].title() + ", you are invited to a lavish banquet at my humble hermitage.")
print("Greetings " + dinner_guests[1].title() + ", you are invited to a lavish banquet at my humble hermitage.")
print("Greetings " + dinner_guests[2].title() + ", you are invited to a lavish banquet at my humble hermitage.")
print("Greetings " + dinner_guests[3].title() + ", you are invited to a lavish banquet at my humble hermitage.")
print("Greetings " + dinner_guests[4].title() + ", you are invited to a lavish banquet at my humble hermitage.")
print("Greetings " + dinner_guests[5].title() + ", you are invited to a lavish banquet at my humble hermitage.")

# Ex 3-6: Tragedy, the new table crumbled to dust upon touching it, now you can only invite 2 guests!
# 1) print out a message announcing this update
# 2) .pop() out guests until you have only 2 left, letting each guest know you can regrettably no longer host them
# 3) print a message to your remaining 2 guests, letting them know they are still invited
# 4) use del to remove the last 2 guests, then print your empty list to be sure
print(25 * "-")
print("Alert! Due to unforeseen and unreasonable events, I am now only capable of hosting a meager meal for 2 guests.")
print(dinner_guests.pop().title() + ", I will see you another time.")
print(dinner_guests.pop().title() + ", I will see you another time.")
print(dinner_guests.pop().title() + ", I will see you another time.")
print(dinner_guests.pop().title() + ", I will see you another time.")
print(dinner_guests[0].title() + ", you are still invited.")
print(dinner_guests[-1].title() + ", you are still invited.")
del dinner_guests[0]
del dinner_guests[0]
print(dinner_guests)
