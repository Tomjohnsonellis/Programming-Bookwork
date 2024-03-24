print("Chapter 3 - Lists")
# Very useful things
print(25 * "-")

my_list = ["apple", "banana", "citrus fruit", "durian", "eggplant"]
print(my_list)
# list indexes start at 0
print(my_list[0])
# the "-1" index is the last one, cool trick!
print(my_list[-1])
# .methods() can also be used with list items
print(my_list[1].upper())
# We can build strings with them as well
print("My favourite fruit is the " + my_list[1].title() + ", I hate " + my_list[-2] + "s!")

print(25 * "-")
# We can also modify the values in lists
my_list[2] = "lemon"
print(my_list)
# Appending things is simple enough
my_list.append(100)
print(my_list)
# As is deleting things
del my_list[3]
print(my_list)
# To /insert/ things at a specific location
my_list.insert(2, "coconut")
print(my_list)
# This has a fun name, pop!
# It "pop"s out the last element in a list, letting you use it then deleting it from the list in one step
print(my_list.pop())
# By specifying an index, you can pop the item at that index!
print(my_list.pop(1))
# Those values are no longer in the list
print(my_list)
# Thankfully you don't always need to know the index value to remove something
my_list.remove("apple")
print(my_list)


