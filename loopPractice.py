num = int(input("Enter a number: "))
count = 1
while count < 11:
    print(str(num) + " x " + str(count) + " = " + str(num*count))
    count += 1

num1 = int(input("Enter a number please: "))
factorial = 1
for number in range(1,num1 + 1):
    factorial = factorial * number

print(factorial)

num2 = int(input("Enter the Number: "))
a = 0
b = 1
variable = 0
if num2 < 0:
    num2 = -num2

while variable < num2:
    if a < num2:
        print(a)
    else:
        break
    c = a + b
    a = b
    b = c
    variable += 1