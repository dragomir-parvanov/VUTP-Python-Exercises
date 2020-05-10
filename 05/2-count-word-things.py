# Write a program to find the number of vowels, consonants, digits and white space characters in a string.

inputString = input("Input a string: ")

vowelsCount = 0
consonantsCount = 0
digitsCount = 0
whiteSpacesCount = 0

for symbol in inputString:
    if symbol.isspace():
        whiteSpacesCount += 1
        continue
    if symbol.isdigit():
        digitsCount += 1
        continue
    if symbol in ["a", "e", "i", "o", "u", "y"]:
        vowelsCount += 1
        continue
    # consonants
    consonantsCount += 1
    
print("Vowels count:",vowelsCount,"Consonants count:",consonantsCount,"Digits count:",digitsCount,"White spaces count:",whiteSpacesCount)