# Write a python program to find number of occurrences of given number without using built-in methods
import functools

numbersList = [1, 1, 1, 3, 3, 3, 2, 2, 4, 4, 5, 6, 7, 7, 7, 9, 10]

numberInput = int(input("Enter a number, to see how much time it is present in the list: "))
lambdaFunction = lambda acc, number: acc+1 if numberInput == number else acc
occurrences = functools.reduce(lambdaFunction, numbersList,0)
print("Occurrences of",numberInput,"is",occurrences)