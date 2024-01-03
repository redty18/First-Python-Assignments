from functools import reduce

numbers = [1,2,3,4,5]

factorial = lambda x, y : x * y

result = reduce(factorial, numbers)
print(result)