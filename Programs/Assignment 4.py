# Program calculates the area of a room and 
# will determine the amount of floor covering needed

# References found on Python documentation 
# Tutor : Tabish Sultan
# https://docs.python.org/3/library/string.html
#   #format-specification-mini-language
# https://docs.python.org/3/library/string.html
#   #format-string-syntaxq
# https://docs.python.org/3/library/stdtypes.html
#   #text-sequence-type-str
# https://python-reference.readthedocs.io/en/latest/docs
#   /operators/semicolon.html
# the semicolon (;) is used as statement separator

print("This program will give you the area of a room")
print("As well as the total of floor covering needed")

print(" Please enter the length of the room in feet")
length = float(input())

print(" Please also enter the width of the room in feet")
width = float(input())
area = length * width 

print(" Here is the area of the room in square feet")
print("{:.2f} sq ft".format(area))

square_yards = area / 9

print(" Here is the area of the room would be in square yards")
print("{:.2f} sq yards".format(square_yards))
