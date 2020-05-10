# Write a program that takes your full name as input and displays the abbreviations of
# the first and middle names except the last name which is displayed as it is.
# For example, if your name is PetarIvanov Petrov, then the output should be P.I.Petrov.

namesInput = input("Enter your names: ")

names = namesInput.split(" ")

print("Hello {0}. {1}. {2}.".format(names[0][0],names[1][0],names[2]))