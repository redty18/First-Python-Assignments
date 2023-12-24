count = 0
sum = 0

for num in range(1,11):
    if num % 2 == 0:
        sum += num
    else:
        count += num

print("\nTest Cases: ")
print("Odd Sum: " + str(count))
print("Even Sum: " + str(sum))

    