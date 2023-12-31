x = int(input("Enter a num: "))
y = int(input("Enter a num: "))
z = int(input("Enter a num: "))
n = int(input("Enter a num: "))

list = []

for num in range(0,x+1):
    for num2 in range(0,y+1):
        for num3 in range(0,z+1):
            if num + num2 + num3 != n:
                list1 = [num,num2,num3]
                list.append(list1)

print(list)