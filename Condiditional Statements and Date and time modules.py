import datetime
current_time = datetime.datetime.now()
print("Current date and time:", current_time)

import calendar
print("\nCalendar for the year 2026:", calendar.calendar(2026))

print("Year:", calendar.isleap(2024))

# To check whether the number is even or odd

number = int(input("Enter a number: "))
print("You entered: {number}")
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

    #bmi calculator
weight= int(input("Enter your weight in kg: "))
height = int(input("Enter your height in cm: "))
bmi = weight / ((height / 100) ** 2)

print("Your BMI is: {bmi}")

if bmi<= 18.5:
    print("You are underweight.")
elif bmi<= 24.9:
    print("You are healthy.")
elif bmi <= 29.9:
    print("You are overweight.")
elif bmi <= 34.9:
    print("You have obesity class I.")
elif bmi <= 39.9:
    print("You have obesity class II.")
else:
    print("You are severely obese.")

