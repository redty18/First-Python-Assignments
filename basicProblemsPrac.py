def sum(a, b):
    return a + b

print(sum(3,5))

def evenOrOdd(a):
    if a % 2 == 0:
        return("Even")
    else:
        return("Odd")
    
print(evenOrOdd(233))

def maxOfThree(a, b, c):
    if (a >= b) and (a >= c):
        max = a
    elif (b >= a) and (b >= c):
        max = b
    else:
        max = c
    return max

print(maxOfThree(1,5,10))

def palindrome(string):
    return string == string[::-1]

print(palindrome("lolo"))

def factorial(nums):
    num1 = 1
    for num in range(1, nums + 1):
        num1 = num1 * num
    return num1

print(factorial(4))



