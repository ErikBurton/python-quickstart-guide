# Define the World Class
class World:
    # Define the greeting
    greeting = "Hello, World!"

    # Run this whenever the object is created
    def __init__(self):
        # Print the greeting
        print(self.greeting)


# Use the class World to crete a world object nameed w
w = World()

# Define the World class another way


class World:
    # Define our greeting
    greeting = "Hello, World!"


print(World.greeting)

# Define a new class


class Customer:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def greet(self):
        print("Hello, " + self.name + "!")


# Create three objects based on the Customer class
c1 = Customer("Sarah", "Atlanta")
c2 = Customer("Erik", "Riverton")
c3 = Customer("Thomas", "Grantsville")

# Add the customer objects to a list
customers = [c1, c2, c3]

# Iterate through list, greet, then display information
for c in customers:
    print()
    c.greet()
    print(c.name + " lives in " + c.city + ".")
