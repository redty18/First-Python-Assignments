# string = "********"
# string2 = ""

# for star in range(1, 12):
#     for i in range(1, star + 1):
#         print("*" + " ",end="")
#     print("\n")

numberInput = int(input("Enter a number: "))
# def multiTable(number,numberInput):
#     for num1 in range(1, numberInput + 1):
#         print(number * num1," ",end='')

for num in range(1, numberInput + 1):
    print("num value : "+ str(num))
    for num1 in range(1, numberInput + 1):
        print(num * num1," ",end='')
    print("\n")