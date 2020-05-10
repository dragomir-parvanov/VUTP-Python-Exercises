# Find the Factorial of a Number

numberInput = int(input("Enter a number: "))

sum = 1

for number in range(1, numberInput + 1):
    sum *= number

print(sum)
