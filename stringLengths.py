strings = ['apple', 'banana', 'cherry', 'date']

length = lambda string : len(string)

result = list(map(length, strings))
print(result)