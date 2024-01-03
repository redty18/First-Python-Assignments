from functools import reduce

numbers = [3, 5, 2, 0, 8, 4]

product = lambda x, y : x * y if x >= 0 and y >= 0 else x

print(reduce(product, numbers))
