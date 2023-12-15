import numpy as np

numbers = [2, 5, 5, 2, 3, 5, 1, 2, 4]
# THis is dictionary

counter = 0
numMap = {}
numMap.clear()

while (counter < len(numbers)):
    numToInsert = numbers[counter]    
    if numToInsert in numMap:
        print(f"Duplicate value {numToInsert}")
        print(numMap)
        returnInsert = numMap.setdefault(numToInsert)
        break

    else:
        returnInsert = numMap.setdefault(numToInsert)
    counter += 1
    
        
        

    