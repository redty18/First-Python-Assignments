# Question 1)
hours = eval(input("Enter hours: "))
rate = eval(input("Enter rate per hour: "))

if hours <= 50:
    pay = hours * rate
else:
    pay = 50 * rate + ((hours - 50) * rate * 2)

print("Pay:", pay)

# Question 2)
score = eval(input("Enter score between 0.0 and 1.0: "))

if 0.0 <= score <= 1.0:
    if score >= 0.9:
        grade = 'A'
    elif score >= 0.8:
        grade = 'B'
    elif score >= 0.7:
        grade = 'C'
    else:
        grade = 'F'
    print("Grade:", grade)
else:
    print("Error: Inputted value out of range")

# Question 3)
largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == 'done':
        break
    try:
        num = int(num)
        if largest == None or num > largest:
            largest = num
        if smallest == None or num < smallest:
            smallest = num
    except ValueError:
        print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)

# Question 4)
num = eval(input("Enter a number: "))

while num > 0:
    print(num, end=' ')
    num -= 1
