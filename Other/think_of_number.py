import random
secret = random.randint(1, 20)

guessing = 0
guess = int(input("Guess a number: "))

while guess != secret:
    guessing += 1

    if guess > secret:
        print("Too high")
    else:
        print("Too low")

    guess = int(input("Guess again: "))

guessing += 1
print(f"you've guessed it correctly, {guess}, it took you {guessing} guesses")
