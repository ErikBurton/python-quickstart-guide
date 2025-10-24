class World:

    # Define out greeting
    greeting = "Hello, World!"

    # Run this whenever the object is created
    def __init__(self):
        # Print the greeting
        print(self.greeting)


# Define a new class
class Customer:

    # Define the init method, using name and city as arguments
    def __init__(self, name, city):
        self.name = name
        self.city = city
# Create three objects based on the Customer class
# The name and city are passed to __ init __


c1 = Customer("Sarah", "Atlanta")
c2 = Customer("Robert", "Florence")
c3 = Customer("Thomas", "Denver")
