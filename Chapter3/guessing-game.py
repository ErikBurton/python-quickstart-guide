from random import randint

# # 1. Generate a random number between 1 and 10
# number = randint(1, 10)

# # 2. Ask for a guess
# guess = int(input("Guess a number between 1 and 10: "))

# # 3. Compare and report result
# if guess == number:
#     print("You got it right! Great job!")
# else:
#     print(f"Sorry, the number was {number}.")

number = randint(1, 100)
attempts = 0

print("I'm thinking of a number between 1 and 100...")

while True:
    guess = int(input("Take a guess: "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Correct! The number was {number}.")
        print(f"You guesses it in {attempts} tries.")
        break




