strings = ['HELLO', 'world', 'PYTHON', 'programming']

uppercaseFilter = lambda string : string.isupper()

print(list(filter(uppercaseFilter, strings)))
