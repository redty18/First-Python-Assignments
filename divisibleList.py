list1 = [1,3,5,7,9,10,13,15,21,25,26,27,28,29,30]

divisible = lambda x : x % 3 == 0 and x % 5 == 0

print(list(filter(divisible, list1)))