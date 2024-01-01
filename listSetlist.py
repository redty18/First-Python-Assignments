def removeDuplicate(list1):
    
    noDuplicate = set(list1)
    newList = list(noDuplicate)
    return newList

myList = [int(x) for x in input("Enter integers separated by spaces: ").split()]
resultingList = removeDuplicate(myList)
print(resultingList)
