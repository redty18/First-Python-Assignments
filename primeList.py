list = [1,3,5,7,9,11,13,15,17,20,23,90,97]
    
def isPrime(number):
    prime = True
    for num in range(2, number):
        if number % num == 0:
           prime = False
    if prime == True:
        return "Prime"
    else:
       return "Not Prime"

def sumOfPrime():
    count = 0
    for num in list:
        if isPrime(num) == "Prime":
            count += num
    return count

print(sumOfPrime())