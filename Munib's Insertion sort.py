from array import array

array = []
upperBound = 0
lowerBound = 0
place = 0
Key = 0

InputDone = False
InputValue = 0


while InputDone == False:

    InputValue = (input("Please enter a value to add to the array or enter an empty string"))
    try:
        int(InputValue)
        array.append(int(InputValue))
    except: 
        InputDone = True
        break
print(array)

upperBound = len(array)


        
for j in range(lowerBound + 1, upperBound):

    Key = array[j]
    place = j - 1
            
    if array[place] > Key:
        
        while place >= lowerBound and array[place] > Key:
            array[place], array[place + 1] = array[place + 1], array[place]
            place -= 1

        array[place + 1] = Key


print (array)