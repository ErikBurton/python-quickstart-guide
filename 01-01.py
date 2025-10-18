price = input("What is the price of a cup of coffee? ")
cups = input("How many cup do you want? ")
total = float(price) * int(cups)
# Be sure to convert to a float and an integer.
print("Your total is $" + str(total) + " for " + cups + " cups.")
