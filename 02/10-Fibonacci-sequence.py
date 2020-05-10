# Python Program to Print the Fibonacci sequence

firstNumber = 0
secondNumber = 1

maxRange = int(input("Maximum Fibonacci sequence iteration: "))
print(0)
print(1)
for _ in range(maxRange):
    fibonacciNumber = firstNumber + secondNumber
    print(fibonacciNumber)
    firstNumber = secondNumber
    secondNumber = fibonacciNumber
