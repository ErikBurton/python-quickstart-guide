#  ClydeBank Coffee Shop Simulator 2112
#  Copyright (C) 2025 ClydeBank Media, All Rights Reserved.

# Import the random module
from random import randint


#  Print welcome message
def welcome():
    print("\nClydeBank Coffee Shop Simulator 2112, Version 1.00")
    print("Copyright (C) 2025 ClydeBank Media, All Rights Reserved.\n")
    print("Let's collect some information before we start the game.\n")


def prompt(display="Please input a string", require=True):

    if require:
        s = False
        while not s:
            s = input(display + " ")
    else:
        s = input(display + " ")
    return s


def convert_to_float(s):
    # If convervion fails, assign 0 to i
    try:
        f = float(s)
    except ValueError:
        f = 0
    return f

def get_weather():
    # Generate a random temperature between 20 and 90
    # We'll consider seasons later on, but this is good enough for now
    return randint(20,90)

# Print Welcome message
welcome()

# Get name and store name
name = prompt("What is your name?", True)
shop_name = prompt("What do you want to name your coffee shop?", True)

# We have what we need, so let's get started!
print("\nOK, let's get started. Have fun!")

# The main game loop
running = True
while running:
    # Display the day and add a "fancy" text effect.
    print("\n-----| Day " + str(day) + " @ " + shop_name + " |-----")

    temperature = get_weather()

    # Display the cash and weather
    daily_stats(cash, temperature, coffee)

    # Get the prince of a cup of coffee
    cup_price = input("What do you want to charge per cup of coffee? ")

    # Get price of a cup of coffee
    print("\nYou can buy advertising to help promote sales.")
    advertising = input("How much advertising do you want to buy? (0 for none)? ")

    # Convert advertising into a float
    # If it fails, assign it to 0
    try:
        advertising = float(advertising)
    except ValueError:
        advertising = 0

    # Deduct advertising from cash on hand
    cash -= advertising

    # TODO: Calculate today's performance
    # TODO: Display today's performance

    # Before we loop around, add a day
    day += 1
