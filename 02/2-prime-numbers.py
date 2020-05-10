# Write a program that prints all prime numbers.

minRange = int(input("Minimum range: "))
maxRange = int(input("Maximum range: "))

# 1(ONE) is not a prime number
if minRange <= 1:
    minRange = 2


for number in range(minRange, maxRange+1):
    prime = True
    for divider in range(2, (number//2)+1):

        if number % divider == 0:
            prime = False
            break
    if prime:
        print(number)
