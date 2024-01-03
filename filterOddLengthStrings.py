
stringLambda = lambda string: len(string) % 2 == 0

strings = ['apple', 'banana', 'cherry', 'date']

result = list(filter(stringLambda, strings))
print(result)

