numbers1 = [5, 8, 10]
numbers2 = [2, 4, 7]

difference = lambda x, y : (x - y) ** 2

print(list(map(difference, numbers1, numbers2)))