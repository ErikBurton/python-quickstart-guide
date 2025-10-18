# name = input("What is your name? ")
# print("Hello, " + name + "!")

word1 = "Hello"
word2 = "World!"
print(word1 + word2)  # No space between words HelloWorld!

word1 = "Hello "  # Adds a space at the end of Hello
word2 = "World!"
print(word1 + word2)

word1 = "Hello"
word2 = "World!"
print(word1 + " " + word2)  # Adds a space inline with print statement

word1 = "Hello"
word2 = "World!"
space = " "  # This works too - but is a bit cumbersome
print(word1 + space + word2)
