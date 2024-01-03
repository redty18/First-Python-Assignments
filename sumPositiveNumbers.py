numbers = [1, -2, 3, -4, 5, -6]

addLambda = lambda x, y : x + y if y > 0 else x

from functools import reduce

result = reduce(addLambda, numbers)
print(result)


