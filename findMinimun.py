from functools import reduce

numbers = [3, 7, 2, 8, 1, 5]

minLambda = lambda x, y : x if x < y else y

result = reduce(minLambda, numbers)
print(result)