is_even = lambda x : x % 2 == 0

list1 = [1,2,3,4,5]

print(list(map(is_even, list1)))

concatenate = lambda string, string2 : string + string2

list2 = ["Hello", "Hi"]
list3 = ["World", "There"]

print(list(map(concatenate, list2, list3)))


customMath = lambda num : num + 10

newList = [1,2,3,4,5]

print(list(map(customMath, newList)))

