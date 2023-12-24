password = str(input("Enter a password: "))
count = 2
passwordMatching = False

for l in range(3):
    passs = str(input("\nEnter password: "))
    if passs != password:
        print("Incorrect password. Attempts left " + str(count - l))
    if passs == password:
        print("Access granted")
        passwordMatching = True
        break

if passwordMatching == False:
    print("Access Denied")