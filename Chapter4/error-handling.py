# Divide a number by zero
a = 7
b = 7

try:
    print(str(a) + " divided by " + str(b) + " is " + str(a/b))
except:
    print("Sorry, a problem occurred dividing the numbers.")

print("All done!")
print(type(a))
print(type(b))