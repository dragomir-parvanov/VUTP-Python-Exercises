# Python Program to Make a Simple Calculator

def applyOperator(number1, operator,number2):
    if currentOperator == "+":
            number1 += float(number2)
    elif currentOperator == "-":
            number1 -= float(number2)
    elif currentOperator == "*":
            number1 *= float(number2)
    elif currentOperator == "/":
            number1 /= float(number2)
    elif currentOperator == "":
            number1 = float(number2)
    else:
             raise Exception("malformed input")
    return number1
        

taskInput = input(
    "Input an expression like 3+1*2. This doesnt support parenthesis and negative numbers, but supports substractions\n")
firtNumber = True
result = 0.00
currentNumber = ""
currentOperator = ""
for char in taskInput:
    if char.isdigit():

        currentNumber += char
    else:
        result = applyOperator(result,currentOperator,currentNumber)
        currentOperator = char
        currentNumber = ""

result = applyOperator(result,currentOperator,currentNumber)

print(taskInput,"=",result)

