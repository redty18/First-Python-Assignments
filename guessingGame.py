import random
secretNum = random.randint(1, 20)
isTrue = True
count = 1
print("Welcome to Number Guessing Game!")

while isTrue:
    guess = int(input("\nGuess the number from 1 to 20: "))
    if guess > secretNum:
        print("Too high. Try again")
        count += 1
    elif guess < secretNum:
        print("Too low. Try again")
        count += 1
    elif guess == secretNum:
        print("Congratulations! You have guessed the correct number in " + str(count) + " tries!")
        isTrue = False


