numbers = [1,2,3,4,5,6,7,8,9]

checkEven = lambda x : x % 2 == 0

result = list(filter(checkEven, numbers))

print(result)