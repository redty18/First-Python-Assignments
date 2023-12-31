def prime(num):
    if num <= 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for num1 in range(1,101):
    if prime(num1):
        print(num1)
