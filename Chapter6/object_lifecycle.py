# class World:

    # Define out greeting
    # greeting = "Hello, World!"

    # Run this whenever the object is created
    # def __init__(self):
    #     # Print the greeting
    #     print(self.greeting)


# Define a new class
# class Customer:

    # Define the init method, using name and city as arguments
    # def __init__(self, name, city):
    #     self.name = name
    #     self.city = city
# Create three objects based on the Customer class
# The name and city are passed to __ init __


# c1 = Customer("Sarah", "Atlanta")
# c2 = Customer("Robert", "Florence")
# c3 = Customer("Thomas", "Denver")


# Define a new class
class Customer:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def __enter__(self):
        print("Entering scope.")
        # Run code upon entereing scope of with statement
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Leaving scope.")
        # Run code upon leaving scope of width statement

    def greet(self):
        print("Hello, " + self.name + "!")


# Use with to create a scope
with Customer("Erik", "Colton") as erik:
    erik.greet()
