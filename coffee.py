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

def x_of_y(x, y):
    num_list = []
    # Return a list of x copies of y
    for i in range(x):
        num_list.append(y)
    return num_list

class CoffeeShopSimulator:

    # Minium and maximum temperatures
    TEMP_MIN = 20
    TEMP_MAX = 90

    
    def __init__(self, player_name, shop_name):
        # Set player and coffee shop names
        self.player_name = player_name
        self.shop_name = shop_name

        # Current day number
        self.day = 1

        # Cash on hand at start
        self.cash = 100.00

        # Inventory at start
        self.coffee_inventory = 100

        # Sales list
        self.sales =[]

        # Possible temperatures
        self.tems = self.make_temp_distribution()

    def run(self):
        print("\nOk, let's get started. Have fun!")

        # The main game loop
        running = True
        while running:
            # Display the day and add a "fancy" text effect
            self.day_header()

            # Get the weather
            temperature = self.weather

            # Display the cash and weather
            self.daily_stats(temperature)

            # Get price of a cup of coffee
            cup_price = float(prompt("What do you want to charge per cup of coffee?"))

            # Get advertising spend
            print("You can buy advertising to help promote sales.")
            advertising = prompt("How much to you want to spend on advertising (0 for none)?" False)

            # Convert advertising into a float
            advertising = convert_to_float(advertising)

            # Deduct advertising from cash on hand
            self.cash -= advertising

            # Simulate today's sales