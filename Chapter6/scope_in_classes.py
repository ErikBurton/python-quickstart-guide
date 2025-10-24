# This vaiable exists in the main scope
name = "Erik"


# Define a new class with a class variable called name
class Customer:
    name = "Krista"


# Creat a new customer so that __init__ is called
customer = Customer()

# Display the name in the main scope
print(customer.name)

# This variable also exists in the main scope
name = "Charles"


# Define a new class with a class variable called name
class Customer:
    def __init__(self, name):
        self.name = name


# Create a new customer so that __init__ is called
customer = Customer("Kim")

# Display the name in the main scope
print(customer.name)
