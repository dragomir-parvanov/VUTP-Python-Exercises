numberList = [32, 37, 28, 30, 37, 25, 27, 24, 35, 55, 23, 31, 55, 21, 40, 18, 50, 35, 41, 49, 37, 19, 40, 41, 31]


sortedNumberList = []


# quicksort???
length = len(numberList)
for i in range(length):
    number = numberList[i]
    placed = False
    for i2 in range(len(sortedNumberList)):
            number2 = sortedNumberList[i2]
            if number >= number2:
                sortedNumberList.insert(i2, number)
                placed = True
                break
            
    if placed is False:
         sortedNumberList.append(number)
        

# my implementation            
print("My implementation of sort()",",".join(map(str, sortedNumberList)))

# checking if its correct, based on the sort() function
print("Native sort()              ",",".join(map(str,reversed(sorted(numberList)))))