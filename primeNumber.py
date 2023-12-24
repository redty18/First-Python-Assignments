Number = int(input("Enter a number: "))
prime = True

for num in range(2, Number):
    # print(Number % num)
    if Number % num == 0:
        prime = False

if prime == True:
    print("Prime Number")
else:
    print(" Not Prime")