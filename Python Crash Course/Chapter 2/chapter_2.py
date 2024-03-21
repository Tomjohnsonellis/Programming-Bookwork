print("Chapter 2")
# Variables - The convention is lower_case_names
print(25*"-")

message = "You can never practice the fundamentals too much."
print(message)
message = "But you must leave your comfort zone to grow."
print(message)  # The same variable has been reassigned!

# String Methods
print(25*"-")

name = "joe bloggs"
print(name)
print(name.title())
print(name.upper())
print(name.upper().lower().title().upper().lower())  # Method chaining!

# String Concatenation
print(25*"-")

forename = "Jim"
surname = "Doe"
full_name = forename + " " + surname
print(full_name)
print("Hello, " + full_name + "!")

# Whitespace
print(25*"-")

print("H\te\tl\tl\to\t!")  # \t for tabs
print("Tic\nTac\nToe")  # \n for newlines
message = "     Whitespace is difficult to see     "
print(message)
print(message.rstrip())  # Removes trailing whitespace
print(message.lstrip())  # Removes preceding whitespace
print(message.strip())  # Removes whitespace from front and back, but not inbetween!

# Numbers
print(25*"-")

print(2 + 3)  # Integers
print(0.5 - 0.3)  # Floats
print(2/3) # Integers are automatically converted as needed
print(10 * 10)
print(10 ** 10) # Python uses ** for "To the power of" instead of ^
print(2 + 3 * 4) # BODMAS Compliant!
print("Happy " + str(100) + "th Birthday!") # Remember: The number 1 is different to the "letter" 1


