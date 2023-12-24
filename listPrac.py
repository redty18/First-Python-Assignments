list = [int(x) for x in input("Enter integers separated by spaces: ").split()]
list2 = []

for num in list:
    if num % 2 == 0:
        list2.append(num)
print(list2)