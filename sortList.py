list = [1,4,5,3,2,6,9,8,7]
# i = 0 
# n = 9
# j = 0
list.sort()
print(list)
def sortAList(numbers):
    n = len(numbers)

    # Go through each number in the list
    for i in range(n):
        # Compare each number with the one next to it
        for j in range(0, n-i-1):
            # Swap the numbers if they are in the wrong order
            if numbers[j] > numbers[j+1]:
                # Swap operation
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    print(numbers)

sortAList(list)

# def switch(x,y):
#     temp = x
#     # temp = 3
#     x = y
#     # x = 9
#     y = temp
#     # y = 3
#     print(x,y)

# switch(3,9)