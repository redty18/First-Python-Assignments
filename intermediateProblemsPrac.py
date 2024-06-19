def Fibonacci(num):
    num1 = 0
    num2 = 1
    next = num2
    count = 0
    while count < num:
        print(next, end=" ")
        num1, num2 = num2, next
        next = num1 + num2
        count += 1

Fibonacci(12)

def listReversal(list):
    reversedList = list[::-1]
    return reversedList

print(listReversal([1,2,3,4,5,6]))

def checkPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return("Not Prime")
        else:
            return("Prime")
print(checkPrime(859))

def listComp(list):
    newList = []
    for num in list:
        newList.append(num ** 2)
    return newList

list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(listComp(list1))

def mergeDict(dict1, dict2):
    return(dict2.update(dict1))

dict3 = {'a': 1, 'b': 2}
dict4 = {'c': 3, 'd': 4}
mergeDict(dict3, dict4)
print(dict4)

