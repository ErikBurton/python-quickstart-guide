# Define the ask function
# def ask(prompt="Please enter a value: "):
#     if prompt.endswith(" "):
#         return input(prompt)
#     else:
#         return input(prompt + " ")


# a = ask()
# b = ask("What do you want for b? ")
# print(a)
# print(b)


# Use the ask function to find out hout many cups we want
# print(ask("How many cups of coffee do you want? "))


# Define the function full_name
def full_name(first="First", middle="Middle", last="Last", display=False):
    name = first + " " + middle + " " + last
    if display:
        print(name)
    return name


# # Use our newly created function
full_name("Charles", "Erik", "Burton", True)
complete_name = full_name("Charles", "Erik", "Burton", False)
print(complete_name)

# x = 5


# def double(n):
#     return n * 2


# x = double(x)
# print(x)
