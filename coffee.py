# ClydeBank Coffee Shop Simulator 2112
# Copyright (C) 2025 ClydeBank Media, All Rights Reserved.

import random


def welcome():
    print("\nClydeBank Coffee Shop Simulator 2112, Version 1.00")
    print("Copyright (C) 2025 ClydeBank Media, All Rights Reserved.\n")
    print("Let's collect some information before we start the game.\n")


def prompt(display="Please input a string", require=True):
    if require:
        s = ""
        while not s:
            s = input(display + " ")
    else:
        s = input(display + " ")
    return s


def convert_to_float(s):
    try:
        return float(s)
    except ValueError:
        return 0.0


def x_of_y(x, y):
    return [y for _ in range(x)]


class CoffeeShopSimulator:
    TEMP_MIN = 20
    TEMP_MAX = 90

    def __init__(self, player_name, shop_name):
        self.player_name = player_name
        self.shop_name = shop_name
        self.day = 1
        self.cash = 100.00
        self.coffee_inventory = 100
        self.sales = []
        self.temps = self.make_temp_distribution()

    def run(self):
        print("\nOk, let's get started. Have fun!")

        running = True
        while running:
            self.day_header()
            temperature = self.weather
            self.daily_stats(temperature)

            cup_price = float(prompt("What do you want to charge per cup of coffee?"))
            print("You can buy advertising to help promote sales.")
            advertising = prompt("How much do you want to spend on advertising (0 for none)?", False)
            advertising = convert_to_float(advertising)

            self.cash -= advertising
            cups_sold = self.simulate(temperature, advertising, cup_price)
            gross_profit = cups_sold * cup_price

            print(f"You sold {cups_sold} cups of coffee today.")
            print(f"You made ${gross_profit:.2f}.\n")

            self.cash += gross_profit
            self.coffee_inventory -= cups_sold
            self.increment_day()

            again = input("Continue to next day? (y/n): ").lower()
            if again != "y":
                running = False
                print(f"\nThanks for playing, {self.player_name}!")

    def simulate(self, temperature, advertising, cup_price):
        cups_sold = self.daily_sales(temperature, advertising)
        self.sales.append({
            "day": self.day,
            "coffee_inv": self.coffee_inventory,
            "advertising": advertising,
            "temp": temperature,
            "cup_price": cup_price,
            "cups_sold": cups_sold
        })
        return cups_sold

    def make_temp_distribution(self):
        temps = []
        avg = (self.TEMP_MIN + self.TEMP_MAX) / 2
        max_dist_from_avg = self.TEMP_MAX - avg

        for i in range(self.TEMP_MIN, self.TEMP_MAX):
            dist_from_avg = abs(avg - i)
            dist_from_max_dist = max_dist_from_avg - dist_from_avg
            if dist_from_max_dist == 0:
                dist_from_max_dist = 1
            temps.extend(x_of_y(int(dist_from_max_dist), i))
        return temps

    def increment_day(self):
        self.day += 1

    def daily_stats(self, temperature):
        print(f"You have ${self.cash:.2f} cash on hand and the temperature is {temperature}.")
        print(f"You have enough coffee on hand to make {self.coffee_inventory} cups.\n")

    def day_header(self):
        print(f"\n------| Day {self.day} @ {self.shop_name} |------")

    def daily_sales(self, temperature, advertising):
        base_sales = max(0, int((self.TEMP_MAX - temperature) * 0.5))
        ad_bonus = int(advertising * 0.5)
        return min(self.coffee_inventory, base_sales + ad_bonus)

    @property
    def weather(self):
        return random.choice(self.temps)


# Start the game
if __name__ == "__main__":
    welcome()
    t_name = prompt("What is your name?", True)
    t_shop_name = prompt("What do you want to name your coffee shop?", True)
    game = CoffeeShopSimulator(t_name, t_shop_name)
    game.run()
