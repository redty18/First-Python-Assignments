isTrue = True
sum = 0

while isTrue:
    num = int(input("Enter a positive number: "))
    if num > 0:
        sum += num
    else:
        isTrue = False

print("Sum of positive numbers: " +str(sum))
