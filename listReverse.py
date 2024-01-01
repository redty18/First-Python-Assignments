list = [1,2,3,4,5]
reversedList = []

for num in list:
    reversedList = [num] + reversedList

print(reversedList)