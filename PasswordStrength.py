# count = 0
containDigit = False

while True:
    password = str(input("Enter a password: "))
    for l in password:
        # count += 1
        if l.isdigit():
            containDigit = True

    if len(password) >= 8 and containDigit == True:
        print("Strong Password")
        break
    else:
        print("Weak Password. Try again!")


            
