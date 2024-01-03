numbers = [2, 7, 15, 23, 9, 10, 11]

def is_Prime(num):
    if num <= 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, n)) # all function used to check if True or False (condition before the for statement)

print(list(filter(is_prime, numbers)))
