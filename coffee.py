#  ClydeBank Coffee Shop Simulator 2112
#  Copyright (C) 2025 ClydeBank Media, All Rights Reserved.
#  Current day number
day = 1
#  Sales list of dictionaries
# #  sales = [
# {
#       "day": 1,
#       "coffee_inv": 100,
#       "advertising": "10",
#       "temp": 68,
#       "cups_sold": 16
# },
# {
#       "day": 2,
#       "coffee_inv": 84,
#       "advertising": "5",
#       "temp": 78,
#       "cups_sold": 10
# },
# {
#       "day": 3,
#       "coffee_inv": 64,
#       "advertising": "5",
#       "temp": 78,
#       "cups_sold": 10
# },
# ]
#  Create an empty sales list
sales = []

#  Print welcome message
print("\nClydeBank Coffee Shop Simulator 2112, Version 1.00")
print("Copyright (C) 2025 ClydeBank Media, All Rights Reserved.\n")
print("Let's collect some information before we start the game.\n")

#  Get name and shop name.
name = input("What is your name? ")
shop_name = input("What do you want to name your coffee shop? ")

print("\nThanks, " + name + "! Let's set some inital pricing.\n")

#  Get initial price of a cup of coffee
cup_price = input("What do you want to charge per cup of coffee? ")

#  Display what we have.
print("\nGreat. Here's what we've collected so far.\n")
print("Your name is " + name + " and you're opening " + shop_name +
      " Coffee Shop!")
print("\nYour first cup of coffee will sell for $" + cup_price + ".\n")
