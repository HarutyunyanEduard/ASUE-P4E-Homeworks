import random

number = random.randint(1,100)
guess = 0
variants = 0
while guess != number and guess != "exit":
    guess = input("Guess my number between 1 and 100\n")

    if guess == "exit":
        break

    guess = int(guess)
    variants += 1

    if guess < number:
        print("Too low!")
    if guess > number:
        print("Too high!")
    if guess == number:
        variants = str(variants)
        print("You win! Number of experiments=" + variants)

