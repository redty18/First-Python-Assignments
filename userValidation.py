validInput = True

while validInput:
    num = input("Enter a number: ")
    if num.isdigit() and int(num) <= 10 and int(num) >= 1:
        print("Valid Input")
    else:
        validInput = False
        print("Not Valid")

