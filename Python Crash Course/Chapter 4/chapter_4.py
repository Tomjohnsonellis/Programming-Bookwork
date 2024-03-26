print("Chapter 4 - Working with Lists")
# More practical uses
print(25 * "-")

pizzas = ["pepperoni", "hawaiian", "margherita", "breakfast"]
# The fundamental list command
for pizza in pizzas:
    print("Today I shall eat a " + pizza + " pizza")

print("I am now very full!")

print(25 * "-")
# Programming and Maths have a lot of overlap, there are some helpful
# commands for number related tasks
for value in range(1, 5):
    print(value)
# Note that 5 was not included, range goes "up to but not including"
# We can store the range for later if we want
numbers = range(5, 11)
print(numbers)
# Oops! We have stored the range command, not the result OF the command
# This can be useful
for x in numbers:
    print(x)
# But what we actually wanted was:
numbers = list(range(11, 16))
print(numbers)
# range(x,y,n) also allows you to skip over numbers,
# or rather, return every nth number in the specified range
multiples_of_5 = list(range(0, 25, 5))
print(multiples_of_5)

print(25 * "-")
# There's also some helpful precoded commands for basic stats
# (Helpful for me being a stats student)
samples = [9, 2, 65, 156, 648, 32, 416, 13, 854, 35, 48, 34, 89, 69,
           18]  # Values chosen by mashing the NumPad and comma key
samples.sort()
print(samples)
# Remember that text and numbers are not the best of friends
print("Min: " + str(min(samples)))
print("Max: " + str(max(samples)))
print("Sum: " + str(sum(samples)))
# For fun let's get the typical stats stuff

mean = sum(samples) / len(samples)
median_position = (len(samples) + 1) * 0.5
# I'm not sure how to code the
# "find the value halfway between two positions" part of a X.5 median
# This was also just for some fun so:
median = samples[int(median_position) - 1]  # - 1 as lists start at Zer0
print("Mean: " + str(mean))
print("Median: " + str(median))
print(sorted(samples))
# The debugger was very helpful here, I should learn to use it properly!

print(25 * "-")
# List comprehensions are introduced here,
# they're like for loops but in a single line, very neat!
cubes = [x ** 3 for x in range(0, 11)]
print(cubes)

print(25 * "-")
# List slices, useful ways to grab sections of a list
people = ["Adam", "Ben", "Charlie", "Douglas", "Esmeralda", "Farnsworth",
          "Garfield", "Hagrid", "Ingrid"]
# Remember: the lists go up to but do not include the 2nd value
# [0:3] would be >012<3
print(people[0:3])
print(people[:3])
print(people[3:6])
print(people[3:])
print(people[-3:])
# Slices are treated the same as a list,
# they're just smaller "sub-lists" if you like
for person in people[2:5]:
    print("Hello my good friend " + person.title() + "!")
# Be careful with assigning lists to new variables
different_list_object = people[:]
same_list_object_but_with_a_new_name = people
# Observe the difference
different_list_object.append("ZZZZZ")
same_list_object_but_with_a_new_name.append("AAAAA")
print(people)
# There are situations where you may want to rename a variable,
# but probably better to rename it globally.
# Developer time is more expensive than computer time,
# "x" is more efficient than "number_used_for_specific_task" but
# if it takes 5 minutes for a developer to work out what "x" is,
# then that efficiency is wasted and then some.
