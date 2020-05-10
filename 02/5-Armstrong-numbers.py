# Find Armstrong Number in an Interval.

minRange = int(input("Minimum range: "))
maxRange = int(input("Maximum range: "))

for number in range(minRange, maxRange + 1):

    # // and % 10 will be more performant
    strNumber = str(number)

    powValue = int(len(strNumber))

    sum = 0
    for digit in strNumber:
        sum += pow(int(digit), powValue)
    if number == sum:
        print("{0} is an Armstrong number".format(number))
