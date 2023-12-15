import numpy as np
num1 = [5,7,9,3]
num2 = [2,4,6,8]
def mySort(intArr01, intArr02):
    intArr03 = intArr01 + intArr02
    intArray = np.array(intArr03)
    i=0
    j=0
    length = len(intArray)
    while (i < length):
        j=i
        while (j < length):
            if intArray[i] > intArray[j]:
                temp = intArray[i]
                intArray[i] = intArray[j]
                intArray[j] = temp

            j += 1
        i += 1
    return intArray
    

num3 = mySort (num1, num2) 
print(num3)
