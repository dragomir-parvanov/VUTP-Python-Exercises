#Write a Python program to find the list of words that are longer than n from a given list of words.

import functools

wordList = ["car", "banana", "corona", "virus"]

maxLetterCountInput = int(input("Max letter count: "))

print(",".join(filter(lambda word : len(word)>maxLetterCountInput,wordList)))