from functools import reduce

strings = ['apple', 'orange', 'banana', 'grape']

concatenate = lambda string, string2 : string + "," + string2

print((reduce(concatenate, strings)))
