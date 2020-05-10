# Write a python program to find the longest word in a given sentence
sentenceInput = input("Input a sentence: ")

currentLongestWord = ""
currentWord = ""
for symbol in sentenceInput:
    if symbol != " ":
        currentWord += symbol
    else:
        if len(currentWord) > len(currentLongestWord):
            currentLongestWord = currentWord
        currentWord = ""

print("The longest word is:",currentLongestWord)
