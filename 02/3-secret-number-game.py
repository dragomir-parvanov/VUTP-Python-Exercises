# Write a guessing game where the user has to guess a secret number.
# After every guess the program tells the user whether their number was too large or too small.
#  At the end the number of tries needed should be printed.
#  It counts only as one try if they input the same number multiple times consecutively.
import random

enteredNumbers = []
randomNumber = random.choice(range(1, 10))


def endGame():
    print("YOU WON!")
    print("It took you " + str(len(enteredNumbers)+1) +
          " unique tries to finish the game!")


def addToEnteredNumbers(number):
    if number not in enteredNumbers:
        enteredNumbers.append(number)


while True:
    numberInput = int(input("Enter your guess: "))

    if numberInput < randomNumber:
        print("The number you entered is too low")
        addToEnteredNumbers(numberInput)
    elif numberInput > randomNumber:
        print("The number you entered is too high")
        addToEnteredNumbers(numberInput)
    else:
        endGame()
        break
