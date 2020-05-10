# Find Factorial of Number Using Recursion


def factorialRecursion(n):
    if n == 1:
        return n
    else:
        return n*factorialRecursion(n-1)


numberInput = int(input("Enter a number: "))

if numberInput < 0:
    print("Factorial does not exist for negative numbers")
elif numberInput == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", numberInput,
          "is", factorialRecursion(numberInput))
