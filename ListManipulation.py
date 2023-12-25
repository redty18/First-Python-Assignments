# list = [1,2,3,4]
# list.append(5)
# print(list)
# list.insert(1,10)
# print(list)
# list.remove(3)
# print(list)

fruits = ["banana", "cherry", "grape" , "xyzk"]
vowel = False

for fruit in fruits:
    for n in fruit:
        if n == "a" or n == "e" or n == "i" or n == "o" or n == "u":
            print(fruit.capitalize())
            break
            
    