import random

variants = 0

number = random.randint(1,100)
print("Guess my number between 1 and 100")

while True:
    print("Ready,steady,go!")   
    guess = input()
    guess = int(guess)

    variants = variants + 1

    if guess < number:
        print("Too low")

    if guess > number:
        print("Too high")

    if guess == number:
        break
    
if guess == number:
    variants = str(variants)
    print("You win! Number of experiments="+variants)
