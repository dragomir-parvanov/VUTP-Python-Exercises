# Count the Number of Each Vowel

sum = 0

print("Caution! We dont count \"y\" as a vowel")

inputString = str(input("Enter a string: "))


for char in inputString:
    char = char.lower()
    if char in ('a', 'e', 'i', 'o', 'u'):
        sum += 1

print("The vowel count is {0}".format(sum))
