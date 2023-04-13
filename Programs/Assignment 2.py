# This program calculates weekly, monthly, and yearly pay based on weekly hours worked and pay rate.
# References:Python Doc and Course Book 
print(" This program calculates weekly, monthly, and yearly pay based on weekly hours worked and pay rate")
print("Please enter number of hours worked")
numOFHours = float(input())
print(" Enter your rate of pay")
ratePerHour = float(input())
week = numOFHours * ratePerHour
month = 52 * week / 12
year = 52 * week
print(" Here is what your weekly pay should be before taxes")
print(numOFHours * ratePerHour)
print(" Here is your monthly pay before taxes")
print(52 * week / 12)
print(" Here is your annual pay before taxes")
print(52 * week)
print(" Thank You For Using Soc's Gross Pay Calculator")
