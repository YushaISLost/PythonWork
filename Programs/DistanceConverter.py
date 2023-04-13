# This program will convert the distance in miles to yards, feet, and inches or kilometers,meters, and centimeters. Depending on the user's preference with yes or no
# Refrences 
# Function definitions: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# Print function: https://docs.python.org/3/library/functions.html#print
# If statements: https://docs.python.org/3/tutorial/controlflow.html#if-statements
# Return Statements https://harpercollege.pressbooks.pub/programmingfundamentals/chapter/return-statement/
# Tutor : Tabish Sultan

def us_standard_lengths(distance_in_miles):
    yards = distance_in_miles * 1760
    feet = distance_in_miles * 5280
    inches = distance_in_miles * 63360
    return yards, feet, inches

def metric_lengths(distance_in_miles):
    kilometers = distance_in_miles * 1.60934
    meters = distance_in_miles * 1609.34 
    centimeters = distance_in_miles * 160934
    return kilometers, meters, centimeters 

distance_in_miles = float(input("Hello please enter the distance in miles: "))
convert_us_standard_lengths = input("Would you like for me to convert the distance in US Standard lengths? (yes/no): ")

if convert_us_standard_lengths == "yes":
    yards, feet, inches = us_standard_lengths(distance_in_miles)
    print("The distance in yards, feet, and inches is:")
    print(yards, "Yards")
    print(feet, "Feet")
    print(inches, "Inches")

else:
    kilometers, meters, centimeters = metric_lengths(distance_in_miles)
    print("The distance in kilometers, meters, and centimeters is:")
    print(kilometers, "Kilometers")
    print(meters, "Meters")
    print(centimeters, "Centimeters")
